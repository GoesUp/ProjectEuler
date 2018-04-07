def run() -> int:
    biggest_palindrome = 0

    for i in range(1000, 100, -1):
        for j in range(i, 100, -1):
            current_product = i * j
            if current_product < biggest_palindrome:
                break
            if str(current_product) == str(current_product)[::-1]:
                biggest_palindrome = current_product
                break

    return biggest_palindrome


if __name__ == "__main__":
    from timeit import default_timer as timer

    start = timer()
    print("Solution:", run())
    print("Duration:", timer() - start)
