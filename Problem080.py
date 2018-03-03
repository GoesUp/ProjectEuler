from decimal import getcontext, Decimal
from math import sqrt

getcontext().prec = 102

seznam = [Decimal(i).sqrt() for i in range(1, 101) if int(sqrt(i)) != sqrt(i)]
vsota = 0
for j in seznam:
    j = [str(j)[0]] + list(str(j))[2:-2]
    vsota += sum([int(k) for k in j])

print(vsota)
