from itertools import permutations


def check(n: int) -> bool:  # Checks if a number is pandigital
    moznosti = [str(i) for i in range(1, len(str(n)) + 1)]
    return set(moznosti) == set(list(str(n))) and len(moznosti) == len(str(n))


def generate(n: int, only: bool = False) -> list:  # generates pandigital numbers from 1 to n
    moznosti = []
    if only:  # if only == True, we will only generate pandigital numbers of length n
        numbers = [str(n)]
    else:
        numbers = [str(i) for i in range(1, n + 1)]
    while len(numbers) > 0:
        moznosti += permutations(numbers, len(numbers))
        numbers.pop()
    return [int("".join(a)) for a in moznosti]
