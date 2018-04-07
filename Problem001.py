def run() -> int:
    multiples = [i for i in range(1, 1000) if ((i % 3 == 0) or (i % 5 == 0))]
    return sum(multiples)

if __name__ == "__main__":
    from timeit import default_timer as timer

    start = timer()
    print("Solution:", run())
    print("Duration:", timer() - start)
