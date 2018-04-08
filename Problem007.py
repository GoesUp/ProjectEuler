import math


def run() -> int:
    prime_quantity = 10001
    biggest_possible = int(prime_quantity * math.log(prime_quantity) * 1.5)
    sito = [True for _ in range(1, biggest_possible)]
    count = 0
    position = 2
    while count < prime_quantity:
        if sito[position]:
            for j in range(2 * position, len(sito), position):
                sito[j] = False
            count += 1
        position += 1

    return position - 1


if __name__ == "__main__":
    from timeit import default_timer as timer

    start = timer()
    print("Solution:", run())
    print("Duration:", timer() - start)
