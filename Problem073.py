from fractions import Fraction
from math import floor, ceil

possibilities = set()
big, small = Fraction(1, 2), Fraction(1, 3)
for i in range(4, 12001):
    for j in range(floor(i * small) + 1, ceil(i * big)):
        ulomek = Fraction(j, i)
        if ulomek >= big:
            break
        possibilities.add(ulomek)
print(len(possibilities))

# SLOW
