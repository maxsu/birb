from hashlib import sha3_512 as H

def segment(text, chunk=3000):
    """Segment text into chunks

    Intelligently segment a long a text into chunks of given size.

    Args:
        text (str): The text to segment
        chunk (int, optional): Maximum segment length. Defaults to 3000.
    """
    def take_chunks(string, n):
        """Chop string into chunks"""
        return [string[i : i + n] for i in range(0, len(string), n)]

    # Initial segmentation
    text = text.strip()
    _segments = text.splitlines()
    if not _segments:
        return []

    # Refine segmentation
    current = _segments[0]
    result = []
    for next in _segments[1:]:
        # Merge short segments
        if len(current+next) < chunk:
            current += "\n" + next
        # Flush current if unable to merge
        if len(current+next) >= chunk:
            result.append(current)
            current = next
        # Merge, chop and flush large segments
        if len(next) > chunk:
            result += take_chunks(current + "\n" + next, chunk)
            current = ''
        assert len(current) < chunk
    result.append(current)
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