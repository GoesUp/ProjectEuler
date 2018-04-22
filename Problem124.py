from functools import reduce
from SieveOfAtkin import sito


def run() -> int:
    primes = sito(100000)
    prime_factors = {1: {1}}
    for i in primes:
        prime_factors[i] = {i}

    for j in range(4, 100001):
        initial_j = j + 0
        if j in prime_factors:
            continue
        counter = 2
        factors = set()
        while True:
            if j == 1:
                break
            if j in prime_factors:
                factors |= prime_factors[j]
                break
            if j % counter == 0:
                factors.add(counter)
                j //= counter
            else:
                counter += 1

        prime_factors[initial_j] = factors

    radicals = []
    for o in primes:
        radicals.append((o, o))
    for k in prime_factors:
        if k not in primes:
            radicals.append((reduce(lambda x, y: x * y, list(prime_factors[k])), k))

    return sorted(radicals)[9999][1]


if __name__ == "__main__":
    from timeit import default_timer as timer

    start = timer()
    print("Solution:", run())
    print("Duration:", timer() - start)
