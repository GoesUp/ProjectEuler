from math import sqrt
from timeit import default_timer


def sito(biggest: int, time: bool = False) -> list:
    start = default_timer()

    solutions = [2, 3]
    primes = dict((i, False) for i in range(5, biggest))

    for x in range(1, int(sqrt(biggest)) + 1):
        for y in range(1, int(sqrt(biggest)) + 1):
            n = 4 * x ** 2 + y ** 2
            if n <= biggest and (n % 12 == 1 or n % 12 == 5):
                primes[n] = not primes[n]
            n = 3 * x ** 2 + y ** 2
            if n <= biggest and n % 12 == 7:
                primes[n] = not primes[n]
            n = 3 * x ** 2 - y ** 2
            if x > y and n <= biggest and n % 12 == 11:
                primes[n] = not primes[n]

    for j in range(5, int(sqrt(biggest)) + 1):
        if primes[j]:
            for k in range(j ** 2, biggest + 1, j ** 2):
                primes[k] = False

    for a in primes:
        if primes[a]:
            solutions += [a]

    if time:
        print(default_timer() - start, "seconds")

    return solutions
