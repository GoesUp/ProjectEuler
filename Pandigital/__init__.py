from itertools import permutations


def check(n: int) -> bool:  # Checks if a number is pandigital
    moznosti = [str(i) for i in range(1, len(str(n)) + 1)]
    return set(moznosti) == set(list(str(n))) and len(moznosti) == len(str(n))


def generate(n: int, only: bool = False) -> list:  # generates pandigital numbers from 1 to n
    moznosti = []
    numbers = [str(i) for i in range(1, n + 1)]
    while len(numbers) > 0:
        moznosti += permutations(numbers, len(numbers))
        if only:
            numbers = []
        else:
            numbers.pop()
    return [int("".join(a)) for a in moznosti]
