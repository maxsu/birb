from collections import UserList
from re import compile

from funtools import Funtools, not_


def limit(n):
    """ Function factory: Break string into pieces of max length n

        n: int > 0
        return: str -> [str]

    """

    if int(n) < 1:
        raise ValueError("needs n > 0")
    regex = f".{{1,{n}}}"
    limiter = compile(regex).findall
    return limiter


class Segment(UserList, Funtools):
    """Segments text for speech by polly
    """

    data = [""]

    @classmethod
    def normalize(cls, text, chunk):
        """ Split each segment at newlines and chunk size

            chunk: int  chunk size (default: 3000)

            Avg segment is smaller than chunk size.

            provides: Each segment is free of newlines
        """
        chunk = str(chunk)

        def merge(res, next):
            choice = len(res) + len(next) < int(chunk)
            if choice:
                res.append(next)
                return res
            else:
                res.add(next)
                return res

        result = cls([text])
        result.catmap(limit(chunk))
        result.catmap(lambda s: s.splitlines())
        result.map(lambda s: s.strip())
        result.filter(not_(compile("^ *$").match))
        result.reduce(merge)

        return result
