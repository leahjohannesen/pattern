from fractions import Fraction
import math
import matplotlib.pyplot as plt
import seaborn as sns

N = 16

class Measurement():
    def __init__(self, dimstr=None, raw=None):
        self.raw = self.parse_str(dimstr) if raw is None else int(raw)

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
        if self.raw > 0:
            return math.floor(self.raw / N), Fraction(self.raw % N, N)
        else:
            return math.ceil(self.raw / N), Fraction(self.raw % N, N)

    @property
    def graph_val(self):
        whole, frac = self.proper
        return whole + float(frac)

    def convert(self, other):
        if isinstance(other, Measurement):
            return other.raw
        return int(other * N)

    def __repr__(self):
        jst = 1 if N < 10 else 2
        whole, frac = self.proper
        sign = ' ' if whole >= 0 else '-'
        wstr = f'{sign}{str(abs(whole)).rjust(2)}'
        if frac.numerator:
            num = str(frac.numerator)
            denom = str(frac.denominator)
        else:
            num, denom = '-', '-'
        return f'{wstr} {num.rjust(jst)}/{denom.rjust(jst)}'

    def __add__(self, other):
        other = self.convert(other)
        return Measurement(raw=self.raw + other)

    def __sub__(self, other):
        other = self.convert(other)
        return Measurement(raw=self.raw - other)

    def __mul__(self, other):
        return Measurement(raw=self.raw * other)

    def __truediv__(self, other):
        return Measurement(raw=self.raw / other)

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

    def __pow__(self, other):
        return Measurement(raw=self.raw ** other)

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
    def __init__(self, a, b, kind=None):
        self.a = a
        self.b = b
        self.kind = kind

    @property
    def length(self):
        x = self.a.x - self.b.x
        y = self.a.y - self.b.y
        return (x ** 2 + y ** 2) ** (1 / 2)

    def dist_along(self, length, ref='a'):
        # returns a point a given distance along a line
        # as measured from 'ref'
        p1 = self.a if 'a' else self.b
        p2 = self.b if 'a' else self.a
        x = p1.x + (p2.x - p1.x) * (length.raw / self.length.raw)
        y = p1.y + (p2.y - p1.y) * (length.raw / self.length.raw)
        return Point(x, y)

    def graph(self):
        x=[self.a.x.raw, self.b.x.raw] 
        y=[self.a.y.raw, self.b.y.raw]

        if self.kind == 'guide':
            color = 'black'
            linestyle = 'dashed'
        elif self.kind == 'temp':
            color = 'red'
            linestyle = 'dashed'
        else:
            color = 'blue'
            linestyle = None

        sns.lineplot(x=x, y=y, color=color, linestyle=linestyle)
        return

    def __repr__(self):
        return f'{self.a} -- {self.b}'


if __name__ == '__main__':
    # print(Measurement('1 2/3'))
    # print(Measurement('4'))
    # print(Measurement('5 6/7'))

    # Measurement('5 6-7')
    # Measurement('8 9 10')

    # blah = Measurement(dimstr='4 3/8')
    # print(blah + 3)
    # print(blah - 3)
    # print(blah * 3)
    # print(blah / 3)
    # print(blah + blah)
    # print(blah - blah)

    # ln = Line(Point('0', '3'), Point('4', '0'))
    # ln.length
    # ln.graph_data()
    # plt.show()

    # a = Measurement('3 3/8')
    # b = Measurement('0')
    # c = b - a
    # print(c, c.raw)

    a = Point('3 3/8', '29 3/4')
    b = Point('9 3/8', '28')
    ln = Line(a, b)
    ln.dist_along(Measurement('4 1/2'))