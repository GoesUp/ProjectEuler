from math import factorial as f

print(sum(True for n in range(1, 101) for r in range(0, n + 1) if (f(n) / (f(r) * f(n - r)) > 1e6)))
