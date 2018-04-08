def run() -> int:
    sum_of_the_squares = sum(i ** 2 for i in range(1, 101))
    square_of_the_sum = sum(j for j in range(1, 101)) ** 2
    return square_of_the_sum - sum_of_the_squares


if __name__ == "__main__":
    from timeit import default_timer as timer

    start = timer()
    print("Solution:", run())
    print("Duration:", timer() - start)
