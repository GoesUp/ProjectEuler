from math import factorial

print(sum([i for i in range(3, 10000000) if sum([factorial(int(j)) for j in str(i)]) == i]))
