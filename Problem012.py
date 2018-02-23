import functools

initial, count = 3, 3
ended = False


def getNumberOfDivisors(n):
    factors = []
    while not n == 1:
        for i in range(2, n + 1):
            if n % i == 0:
                factors += [i]
                n = n // i
                break

    razlicne_potence = list(set(factors))
    ponavljanje = [factors.count(x) for x in razlicne_potence]

    return functools.reduce(lambda x, y: x * y, list(map(lambda w: w + 1, ponavljanje)))


while not ended:
    initial += count
    count += 1
    if getNumberOfDivisors(initial) > 500:
        print(initial)
        ended = True
    else:
        pass
