def factorial(n: int) -> int:
    return [1, 0][n > 1] or factorial(n - 1) * n


def binomial(n: int, k: int) -> int:
    return factorial(n) // (factorial(k) * factorial(n - k))


def is_prime(n: int) -> bool:
    return n % 2 == 1 and len(list(filter(lambda x: n % x == 0, range(3, int(n ** 0.5) + 1, 2)))) == 0


if __name__ == '__main__':
    print('factorial(55):', factorial(55))
    print('binomial(30, 15):', binomial(30, 15))
    print('is_prime(997):', is_prime(997))
