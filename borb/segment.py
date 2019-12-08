from collections import UserList
from itertools import chain
cat = chain.from_iterable
import json, re
from pathlib import Path
print(Path.cwd())
conf = 'borb/borbConfig.json'
opt = json.loads(Path(conf).resolve().read_text())
CHUNK = opt['chunk']

class Segment(UserList):
    """Segments text for speech by polly
    """
    def __init__(self, text):
        self.data = [text]

    def split(self, chunk):
        split = re.compile(f".{{1,{chunk}}}").findall
        self.data = map(lambda s: s.strip(),
                        cat(map(split, self.data)))
        return self

    def drop(self, regex="^ *$"):
    # default: drop empty segments
        test = lambda x: not re.match(regex, x)
        self.data = list(filter(test, self.data))
        return self
    
    @staticmethod
    def normalize(text):
        return Segment(text).split(CHUNK).drop()
