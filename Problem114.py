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
        # If the row is shorter than three units, there is only one possibility (we can't fit any red in there)
        if n < 3:
            return 1

        # Count the possibilities if the first square is black
        crna = recursion(n - 1)

        # Count the possibilities if we use the red blocks of all possible sizes
        rdece = [recursion(n - i - 1) for i in range(3, n + 1)]

        # Sum up the possibilities and return
        return crna + sum(rdece)

    return recursion(50)


if __name__ == "__main__":
    from timeit import default_timer as timer

    start = timer()
    print("Solution:", run())
    print("Duration:", timer() - start)
