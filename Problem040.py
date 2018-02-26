from functools import reduce

decimalke = "".join([str(i) for i in range(1, 300000)])

print(reduce(lambda x, y: x * y, [int(decimalke[(10 ** i) - 1]) for i in range(7)]))
