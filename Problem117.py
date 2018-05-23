def run() -> int:
    class Memo:

        def __init__(self, f):
            self.f = f
            self.memo = {}

        def __call__(self, *args):
            if args not in self.memo:
                self.memo[args] = self.f(*args)
            return self.memo[args]

    @Memo
    def recursion(n):
        # This code was adapted from problem 114.

        # If the row is shorter than two units, there is only one possibility
        if n < 2:
            return 1

        # Count the possibilities if the first square is black
        crna = recursion(n - 1)

        # If there is enough room, try fitting in the colored tiles
        rdeca, zelena, modra = 0, 0, 0

        if n >= 2:
            rdeca = recursion(n - 2)
            if n >= 3:
                zelena = recursion(n - 3)
                if n >= 4:
                    modra = recursion(n - 4)

        return crna + rdeca + zelena + modra

    return recursion(50)


if __name__ == "__main__":
    from timeit import default_timer as timer

    start = timer()
    print("Solution:", run())
    print("Duration:", timer() - start)
