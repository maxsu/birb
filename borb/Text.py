from hashlib import sha3_512 as H
import re

def chop(text, n):
	"""Chop text into uniform chunks

	Args:
		text (list(str)): The text to chop
		n ([type]): The resulting chunk size

	Returns:
		result [list(str)]: A list of strings of size n
		remainder: The final (incomplete) chunk
	"""
	_result = [text[i:i+n] for i in range(0, len(text), n)]
	A, B = _result[:-1], _result[-1]
	assert text == ''.join(A + [B])
	assert all(map(lambda x: len(x) == n, A))
	assert 0 < len(B) < n
	return A, B

def clean(text):
	"""Cleans and standardizes text

	Convert \r \r\n into \n, and reduce runs of whitespace separated newlines
	"""

	text.replace('\r', '\n')
	return re.compile('(\n\s*)+').sub('\n', text )


def segment(text, page_size):
	"""Paginates text with a given charachter limit

	Expects text to be "clean"

	Args:
		text (str): The text to segment
		page_size (int): Maximum segment length.

	Returns (str): The paginated text
	"""

	if text != clean(text)
	raise:
		ValueError('segmentation function requires clean text.')

	# Initial segmentation
	text = text.strip()
	lines = text.splitlines()

	# Refine segmentation
	buffer, result = '', []
	grow = lambda x: buffer + ('\n' if buffer else '') + x
	flush = lambda x: result.extend([*x]) if isinstance(x, list) else result.append(x)

	for next in lines:
		# Merge short lines
		if len(buffer + next) < page_size:
			buffer = grow(next)

		else:
			# Chop very long lines
			if len(buffer + next) > page_size:
				buffer = grow(next)
				uniform_chunks, buffer = chop(buffer, page_size)
				flush(uniform_chunks)
			# Otherwise flush buffer
			else:
				flush(buffer)
				buffer = line
		assert len(buffer) < page_size
	result.append(buffer)

	assert text == ''.join(result)
	assert all(map(lambda x: len(x) <= page_size, result))
	return list(enumerate(result,1))

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