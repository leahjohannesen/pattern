from fractions import Fraction
import math

N = 8

class Measurement():
    def __init__(self, dimstr=None, raw=None):
        self.raw = self.parse_str(dimstr) if raw is None else raw
        if isinstance(self.raw, float):
            print(dimstr, raw)
            raise

    def parse_str(self, dimstr):
        try:
            wstr, fstr = dimstr.split(' ')
        except ValueError:
            wstr = dimstr
            fstr = '0/1'

        try:
            num, denom = fstr.split('/')
        except ValueError:
            raise Exception(f'Bad input detected, please retry | {dimstr}')

        try:
            return int(wstr) * N + int(N * int(num) / int(denom))
        except:
            raise Exception(f'Bad input detected, please retry | {dimstr}')

    @property
    def proper(self):
        return math.floor(self.raw / N), Fraction(self.raw % N, N)


    def convert(self, other):
        if isinstance(other, Measurement):
            return other.raw
        return int(other * N)

    def __repr__(self):
        whole, frac = self.proper
        return f'{whole} {frac}'

    def __add__(self, other):
        other = self.convert(other)
        if isinstance(self.raw + other, float):
            print(f'{self} + {other}')
            raise
        return Measurement(raw=self.raw + other)

    def __sub__(self, other):
        other = self.convert(other)
        return Measurement(raw=self.raw - other)

    def __mul__(self, other):
        return Measurement(raw=self.raw * other)

    def __truediv__(self, other):
        return Measurement(raw=int(self.raw / other))

    def __lt__(self, other):
        other = self.convert(other)
        return self.raw < other

    def __le__(self, other):
        other = self.convert(other)
        return self.raw <= other
    
    def __gt__(self, other):
        other = self.convert(other)
        return self.raw > other
    
    def __ge__(self, other):
        other = self.convert(other)
        return self.raw >= other

class Point():
    def __init__(self, x, y):
        x, y = self.maybe_convert(x, y)
        self.x = x
        self.y = y

    def maybe_convert(self, x, y):
        if not isinstance(x, Measurement):
            x = Measurement(x)
        if not isinstance(y, Measurement):
            y = Measurement(y)
        return x, y
    
    def dupe(self):
        return Point(self.x, self.y)

    def __add__(self, other):
        # adds a tuple of (x, y)
        return Point(self.x + other[0], self.y + other[1])

    def __sub__(self, other):
        # adds a tuple of (x, y)
        return Point(self.x - other[0], self.y - other[1])

    def __repr__(self):
        return f'({self.x}, {self.y})'

class Line():
    def __init__(self, a, b, label):
        self.a = a
        self.b = b
        self.label = label



if __name__ == '__main__':
    print(Measurement('1 2/3'))
    print(Measurement('4'))
    print(Measurement('5 6/7'))

    # Measurement('5 6-7')
    # Measurement('8 9 10')

    blah = Measurement(dimstr='4 3/8')
    print(blah + 3)
    print(blah - 3)
    print(blah * 3)
    print(blah / 3)
    print(blah + blah)
    print(blah - blah)
