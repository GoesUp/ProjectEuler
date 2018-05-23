import sys

sys.setrecursionlimit(15000)


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

        # If the row is shorter than three units, there is only one possibility (we can't fit any red in there)
        if n < 3:
            return 1

        # Count the possibilities if the first square is black
        crna = recursion(n - 1)

        # Count the possibilities if we use the red blocks of all possible sizes from 50 onwards
        rdece = [recursion(n - i - 1) for i in range(50, n + 1)]

        # Sum up the possibilities and return
        return crna + sum(rdece)

    n = 50
    while True:
        # Start checking at n = 50. If fill_count is too small, try for next n
        fill_count = recursion(n)
        if fill_count > 1e6:
            return n
        n += 1


if __name__ == "__main__":
    from timeit import default_timer as timer

    start = timer()
    print("Solution:", run())
    print("Duration:", timer() - start)
