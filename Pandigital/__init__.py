from itertools import permutations


def check(n: int) -> bool:  # Checks if a number is pandigital
    moznosti = [str(i) for i in range(1, len(str(n)) + 1)]
    return set(moznosti) == set(list(str(n))) and len(moznosti) == len(str(n))


def generate(n: int, only: bool = False, incl_zero: bool = False, excluded: list = []) -> list:  # generates pandigital numbers from 1 to n
    moznosti = []
    if incl_zero:
        numbers = [str(i) for i in range(0, n + 1)]
    else:
        numbers = [str(i) for i in range(1, n + 1)]
    if list:
        numbers = sorted(list(set(numbers) - set(map(str, excluded))))
    while len(numbers) > 0:
        moznosti += permutations(numbers, len(numbers))
        if only:
            numbers = []
        else:
            numbers.pop()
    return sorted(list(set([int("".join(a)) for a in moznosti])))
