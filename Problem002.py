def run() -> int:
    first, second, vsota_sodih = 1, 2, 2

    while second < 4 * 10 ** 6:
        first, second = second, first + second
        if second % 2 == 0:
            vsota_sodih += second

    return vsota_sodih

if __name__ == "__main__":
    from timeit import default_timer as timer

    start = timer()
    print("Solution:", run())
    print("Duration:", timer() - start)
