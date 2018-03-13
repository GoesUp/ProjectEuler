class Memo:

    def __init__(self, f):
        self.f = f
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]


penta = lambda x: x * (3 * x - 1) // 2
penta_test = lambda x: ((24 * x + 1) ** 0.5 + 1) / 6  # obtained from "Pentagonal number" on Wikipedia


@Memo
def gen_penta(n):
    return penta_test(n)


@Memo
def is_penta(n):
    temp = penta_test(n)
    valid = temp == int(temp)
    return valid


def search():
    counter = 2
    while True:
        current = penta(counter)
        for i in range(1, counter):
            comparing_penta = penta(i)
            if is_penta(abs(current - comparing_penta)) and is_penta(comparing_penta + current):
                return current - comparing_penta
        counter += 1


print(search())
