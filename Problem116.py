def run() -> int:
    class Memo:

        def __init__(self, f):
            self.f = f
            self.memo = {}

        def __call__(self, *args, **kwargs):
            if (args, kwargs['color']) not in self.memo:
                self.memo[(args, kwargs['color'])] = self.f(*args, **kwargs)
            return self.memo[(args, kwargs['color'])]

    @Memo
    def recursion(n, color=None):
        # This code was adapted from problem 114.

        # If the row is shorter than two units, there is only one possibility
        if n < 2:
            return 1

        # If the color has not yet been asigned and only two tiles are left, assign color red to it.
        if n == 2 and color == None:
            return 1

        barva = color

        # Count the possibilities if the first square is black
        crna = recursion(n - 1, color=barva)

        rdeca, zelena, modra = 0, 0, 0

        # If one of the colors was already used, only consider tiles of the same color from now on
        if n >= 2 and (color == 'red' or color == None):
            rdeca = recursion(n - 2, color='red')
        if n >= 3 and (color == 'green' or color == None):
            zelena = recursion(n - 3, color='green')
        if n >= 4 and (color == 'blue' or color == None):
            modra = recursion(n - 4, color='blue')

        return crna + rdeca + zelena + modra

    return recursion(50, color=None)


if __name__ == "__main__":
    from timeit import default_timer as timer

    start = timer()
    print("Solution:", run())
    print("Duration:", timer() - start)
