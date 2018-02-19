import functools

numbers = [i for i in range(11, 21)]
vsota = sum(numbers)
top_limit = functools.reduce(lambda x, y: x * y, numbers)
for j in range(20, top_limit, 20):
    if all([j % k == 0 for k in numbers]):
        print(j)
        break

# UGLY
