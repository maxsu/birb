from dataclasses import dataclass
from itertools import chain

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
    """ Appendable list of strings: [str]

        Used as state for reduce

        val: List of strings

        __len__: Length of latest string in val
        
        append: Append to latest string
        
        add: Add new string to end of val
    """
    def __init__(val):
        if not val:
            self.val = [""]
        else:
            self.val = val

    def __len__(self):
        return len(self.val[-1])
    
    def append(self, next):
        val = self.val
        val[-1] += "\n" + next
        return _Res(val)

    def add(self, next):
        val = self.val
        val += [next]
        return _Res(val)

    def if_(self, f, val):
        if f(self): return self.append(val)
        else: return self.add(val)


class Funtools:

    def map(self, f):
        return self.__init__(map(f, self.data))
    
    def catmap(self, f):
        return self.__init__(cat(map(f, self.data))
    
    def filter(self, f):
        return self.__init__(filter(f, self.data)

    def reduce(self, f):
        result = reduce(f, self.data, _Res()).val
        return self.__init__(result)
