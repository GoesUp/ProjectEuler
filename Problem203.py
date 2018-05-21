from functools import reduce
from eulerlib import primes


def run() -> int:
    # Generate squares of primes. Primes up to ten will suffice - we only use factorials up to 51, which means
    # numbers in this problem can't be divisible by primes higher than that
    pra = [a ** 2 for a in primes(10)]

    # Define functions for calculating the factorial, the binomial coefficient and checking whether a number is prime
    def factorial(n: int) -> int:
        if n == 0:
            return 1
        else:
            return reduce(lambda x, y: x * y, list(range(1, n + 1)))

    prime = lambda y: y % 2 == 1 and len(list(filter(lambda x: y % x == 0, range(3, int(y ** 0.5) + 1, 2)))) == 0
    binomial = lambda n, k: factorial(n) // (factorial(k) * factorial(n - k))

    # Initialize the set for storing all numbers that appear in the Pascal triangle and then fill the said set
    pascal = set()

    for i in range(51):
        for j in range(i // 2 + 1):
            pascal.add(binomial(i, j))

    # Check all numbers stored in 'pascal' and store the valid ones into 'valid'
    valid = set()
    for j in sorted(pascal):
        if prime(j):
            # If the number itself is prime, it cannot be divided by any square of a prime. Add it to the valid ones.
            valid.add(j)
        else:
            # If any of the prime squares divide the number we're currently checking, add that number to 'valid'
            if not any(j % k == 0 for k in pra):
                valid.add(j)

    # Finally, return the sum of the squarefree numbers
    return sum(valid)


if __name__ == "__main__":
    from timeit import default_timer as timer

    start = timer()
    print("Solution:", run())
    print("Duration:", timer() - start)
