from fractions import Fraction
from functools import reduce

final_fractions = []
for i in range(10, 100):
    for j in range(10, 100):
        if i % 10 != 0 and j % 10 != 0:
            temp_i, temp_j = str(i), str(j)
            if temp_i[0] == temp_j[0]:
                if Fraction(i, j) == Fraction(int(temp_i[1]), int(temp_j[1])):
                    final_fractions.append(Fraction(i, j))
            elif temp_i[1] == temp_j[0]:
                if Fraction(i, j) == Fraction(int(temp_i[0]), int(temp_j[1])):
                    final_fractions.append(Fraction(i, j))
            elif temp_i[1] == temp_j[1]:
                if Fraction(i, j) == Fraction(int(temp_i[0]), int(temp_j[0])):
                    final_fractions.append(Fraction(i, j))

print(reduce(lambda a, b: a * b, list(set(final_fractions))).denominator)
