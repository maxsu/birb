from itertools import chain
from functools import reduce

cat = chain.from_iterable


class wrapper:
    def wrap(self, f):
        def ff(*xargs, **kargs):
            val = f(*xargs, *kargs)
            a = self.__init__()
            a.data = val
            return a


def not_(f):
    return lambda *x: not f(*x)


class _Res:
    """ Reducer state. Appendable list of strings.

        val: List of strings
        __len__: Length of last string in val
        append: Append to last string
        add: Add new string to end of val
    """
    def __init__(self, val=None):
        if not val:
            self.val = [""]
        else:
            self.val = val

    def __len__(self):
        return len(self.val[-1])

    def append(self, next):
        self.val[-1] += "\n" + next
        return self

    def add(self, next):
        self.val += [next]
        return self


class Funtools:

    def map(self, f):
        self.data = list(map(f, self.data))
        return self

    def catmap(self, f):
        self.data = list(cat(map(f, self.data)))
        return self

    def filter(self, f):
        self.data = list(filter(f, self.data))

        return self

    def reduce(self, f):
        self.data = reduce(f, self.data, _Res()).val
        return self
