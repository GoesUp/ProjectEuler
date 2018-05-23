def run() -> int:
    def is_bouncy(n):
        # We will use this function to determine whether the number is bouncy or not.
        decrease, increase = 0, 0
        for i in range(len(n) - 1):
            if n[i] < n[i + 1]:
                increase += 1
            elif n[i] > n[i + 1]:
                decrease += 1
            if decrease and increase:
                return True
        return False

    bouncy = 0
    i = 100
    while True:
        # Convert the number to a list with which the 'is_bouncy' function can operate
        i_list = [int(j) for j in str(i)]

        # If the number is bouncy, we note that another number is bouncy
        if is_bouncy(i_list):
            bouncy += 1

        # If there are enough bouncy numbers, we return the needed amount of checked numbers
        if bouncy / i == 0.99:
            return i
        i += 1


if __name__ == "__main__":
    from timeit import default_timer as timer

    start = timer()
    print("Solution:", run())
    print("Duration:", timer() - start)
