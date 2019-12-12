from dataclasses import dataclass
from collections import UserList
from functools import reduce
from itertools import chain
import json
from pathlib import Path
import re

cat = chain.from_iterable

class Res:

    def __init__(self, val = None):
        if not val:
            val = [""]
        self.val = val

    def __len__(self):
        return len(self.val[-1])

    def append(self, next):
        self.val[-1] += "\n" + next
        return self
        
    def add(self, next):
        self.val += [next]
        return self

class Segment(UserList):
    """Segments text for speech by polly
    """

    def __init__(self, text='', data=[]):
        if data:
            self.data = list(data)
        else:
            self.data = [text]

    def split(self, chunk):
        """ Split each segment at newlines and chunk size

            chunk: int  chunk size (default: 3000)

            Avg segment is smaller than chunk size.

            provides: Each segment is free of newlines
        """
        
        regex = f".{{1,{chunk}}}"
        findall = re.compile(regex).findall

        self.data = cat([s.splitlines() for s in self.data])
        self.data = cat(map(findall, self.data))
        self.data = [s.strip() for s in self.data]
        return self
   
    def drop(self, regex="^ *$"):
        """ Drop segments that match a regex

            assumes: strings have no newlines chars

            regex: defaults to match empty or whitespace-only strings
        """
        # default: drop empty segments
        def test(x): return not re.match(regex, x)
        self.data = list(filter(test, self.data))
        return self

    def merge(self, chunk):
        """ Split each segment at newlines and chunk size

            chunk: int  chunk size (default: 3000)
        """
        def merge_(res, next):
            if len(res) + len(next) < chunk:
                return res.append(next)
            else:
                return res.add(next)

        self.data = reduce(merge_, self.data, Res()).val
        return self

    @staticmethod
    def normalize(text, chunk):
        return (
            Segment(text)
                .split(chunk)
                .drop()
                .merge(chunk)
        )