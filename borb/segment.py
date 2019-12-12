from dataclasses import dataclass
from collections import UserList
from functools import reduce
import json
from pathlib import Path
import re

from funtools import Funtools, not_


class Segment(UserList, Funtools):
    """Segments text for speech by polly
    """

    data = [""]

    @staticmethod
    def normalize(cls, text, chunk):
        """ Split each segment at newlines and chunk size

            chunk: int  chunk size (default: 3000)

            Avg segment is smaller than chunk size.

            provides: Each segment is free of newlines
        """
        split = lambda s: s.splitlines()
        findall = re.compile(".{1," + chunk + "}").findall
        strip = lambda s: s.strip()
        drop = not_(re.compile("^ *$").match)
        merge = lambda res, next: \
            res.if_(lambda s: len(s) + len(next) < chunk, 
                    next)

        return (Segment(split(text))
                     .catmap(findall)
                     .map(strip)
                     .filter(drop)
                     .reduce(merge))