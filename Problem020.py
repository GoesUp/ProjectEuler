import functools

print(sum([int(b) for b in str(functools.reduce(lambda x, y: x * y, [a for a in range(2, 101)]))]))
