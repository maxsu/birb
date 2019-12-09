from collections import UserList
from functools import reduce
from itertools import chain
import json
from pathlib import Path
import re

cat = chain.from_iterable
print(Path.cwd())

conf = 'borb/borbConfig.json'
opt = json.loads(Path(conf).read_text())

class Res:
    def __init__(self):
        self.count = 0
        self.current = [""]

    def append(self, next):
        self.current[-1] += "\n" + next
        self.count += len(next) + 1

    def add(self, next):
        self.current += [next]
        self.count = len(next)


def greedyMerge(res, next):
    if res.count + len(next) < 3000:
        res.append(next)
    else:
        res.add(next)
    return res


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

    def merge(self):
        self.data = reduce(greedyMerge, self.data, Res()).current
        return self

    def drop(self, regex="^ *$"):
        # default: drop empty segments
        def test(x): return not re.match(regex, x)
        self.data = list(filter(test, self.data))
        return self

    @staticmethod
    def normalize(text):
        return Segment(text).split(opt['chunk']).drop().merge()
