from fractions import Fraction


class Memo:

    def __init__(self, f):
        self.f = f
        self.saved = {}

    def __call__(self, *args):
        if args not in self.saved:
            self.saved[args] = self.f(*args)
        return self.saved[args]


@Memo
def iterations(n):
    if n == 1:
        return Fraction(2)
    return Fraction(2 + Fraction(1 / iterations(n - 1)))


def wrapper(n):
    temp = Fraction(1 + 1 / iterations(n))
    return temp.numerator, temp.denominator


how_many = 0
for i in range(1, 1001):
    a, b = wrapper(i)
    if len(str(a)) > len(str(b)):
        how_many += 1

print(how_many)
