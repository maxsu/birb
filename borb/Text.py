from hashlib import sha3_512 as H
import re
from dataclasses import dataclass
from pathlib import Path

def clean(text):
	"""Cleans and standardizes text

	Convert \r \r\n into \n, and reduce runs of whitespace separated newlines
	"""

	text = text.replace('\r', '\n')
	return re.compile('(\n\s*)+').sub('\n', text )


def take(s, n):
	"""Return first n characters of a list, and the remainder

	Args:
		s (string): a string to split
		n (int): a position to split at

	Returns
	    take (str): The first n characters
		remainder (str):  The rest of the string
	"""
	A, B = s[:n], s[n:]
	assert s == A + B
	return A, B


@dataclass
class Page:
	text: str = ''
	id: str = ''
	num: int = 1
	mp3: Path = None

	def __len__(self):
		return self.text.__len__()

	def __str__(self):
		return self.text


def paginate(text, page_limit):
	"""Paginates text with a given character limit

	Expects text to be "clean"

	Args:
		text (str): The text to segment
		page_size (int): Maximum segment length.

	Returns (str): The paginated text
	"""

	if text != clean(text):
		raise ValueError('Pagination requires clean text.')

	# Initial segmentation
	text = text.strip()
	lines = text.splitlines()

	# Refine segmentation
	pages, 	page_num, temp_page =	[], 1, ''
	_flush = lambda x: pages.append(Page(num=page_num, text=x))

	for line in lines:
		# Padding adds a spoken pause between lines.
		pad = '\n' if temp_page else ''
		temp_page += pad + line

		while len(temp_page) >= page_limit:
			page, temp_page = take(temp_page, page_limit)
			_flush(page)
			page_num += 1

		assert len(temp_page) < page_limit

	if temp_page:
		_flush(temp_page)

	front_pages, final_page = take(pages, -1)

	assert all([len(a) == page_limit for a in front_pages])
	assert len(final_page) < page_limit
	assert text == ''.join(map(lambda p: p.text, pages))

	return [(p.num, p.text) for p in pages]

def template(template_string):
	def _template(arguments):
		print(template_string.format(*arguments))
	return _template

def insert(A, B, i):
	return B[:i] + A + B[i:]

def part_number(text, shape, spacer='-'):
	# Surprisingly this actually works!
	shape.sort(reverse=True)
	for offset in shape:
		text = insert(spacer, text, offset)
	return text

def digest(text):
	return H(text.encode()).hexdigest()

def speech_id(text):
	return part_number(digest(text)[:24], [2,4,8,16])