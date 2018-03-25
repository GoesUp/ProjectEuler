class Memo:

    def __init__(self, f):
        self.f = f
        self.seznam = {}

    def __call__(self, *args):
        if args not in self.seznam:
            self.seznam[args] = self.f(*args)
        return self.seznam[args]


@Memo
def sum_of_divisors(n):
    return sum(i for i in range(1, n + 1) if n % i == 0)


@Memo
def particije(n):
    if n == 0 or n == 1:
        return 1
    return (1 / n) * sum(sum_of_divisors(n - a) * particije(a) for a in range(n))


print(int(particije(100)) - 1)
