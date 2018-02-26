from itertools import permutations

permutacije = list(permutations("0123456789", 10))
print("".join(permutacije[999999]))
