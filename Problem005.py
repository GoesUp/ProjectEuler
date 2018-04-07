from functools import reduce
from math import gcd


def run() -> int:
    numbers = [i for i in range(11, 21)]
    return reduce(lambda x, y: x * y // gcd(x, y), numbers)


if __name__ == "__main__":
    from timeit import default_timer as timer

    start = timer()
    print("Solution:", run())
    print("Duration:", timer() - start)
