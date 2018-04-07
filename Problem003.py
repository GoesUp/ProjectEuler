def run() -> int:
    highest_factor = 3
    number = 600851475143

    while not number == 1:
        for i in range(highest_factor, number + 1, 2):
            if number % i == 0:
                highest_factor = i
                number = number // i
                break

    return highest_factor

if __name__ == "__main__":
    from timeit import default_timer as timer

    start = timer()
    print("Solution:", run())
    print("Duration:", timer() - start)
