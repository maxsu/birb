from collections import UserList
from itertools import chain
import json
from pathlib import Path
import re

cat = chain.from_iterable
print(Path.cwd())

conf = 'borb/borbConfig.json'
opt = json.loads(Path(conf).read_text())


class Segment(UserList):
    """Segments text for speech by polly
    """

    def __init__(self, text='', data=[]):
        if data:
            self.data = list(data)
        else:
            self.data = [text]

    def split(self, chunk):
        regex = f".{{1,{chunk}}}"
        findall = re.compile(regex).findall
        self.data = cat(map(findall, self.data))
        self.data = [s.strip() for s in self.data]
        return self

    def drop(self, regex="^ *$"):
        # default: drop empty segments
        def test(x): return not re.match(regex, x)
        self.data = list(filter(test, self.data))
        return self

    @staticmethod
    def normalize(text):
        return Segment(text).split(opt['chunk']).drop().merge()
