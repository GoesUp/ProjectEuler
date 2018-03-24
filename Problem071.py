from fractions import Fraction

maksimum, minimum = Fraction(3, 7), Fraction(28, 70)
for i in range(1, int(1e6)):
    for j in range(int(i * minimum) - 1, int(i * maksimum) + 10):
        trenutni_ulomek = Fraction(j, i)
        if trenutni_ulomek >= maksimum:
            break
        if trenutni_ulomek > minimum:
            minimum = trenutni_ulomek

print(minimum.numerator)
