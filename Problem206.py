def run() -> int:
    low = int(10203040506070809 ** .5)
    static = "123456789"
    while True:
        if str(low ** 2)[::2] == static:
            return low * 10
        low += 2


if __name__ == "__main__":
    from timeit import default_timer as timer

    start = timer()
    print("Solution:", run())
    print("Duration:", timer() - start)
