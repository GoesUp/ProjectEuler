class Memo:

    def __init__(self, f):
        self.f = f
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]


@Memo
def get_prime_factors(n):
    if n == 1:
        return []
    else:
        i = 2
        while i < n // 2 + 1:
            if not n % i:
                return list(set(get_prime_factors(n // i)).union([i]))
            i += 1
        return [n]


counter = 2
while True:
    dolzine = [len(get_prime_factors(w)) for w in range(counter, counter + 4)]
    if sum(dolzine) == 16:
        print(counter)
        break
    counter += 1
