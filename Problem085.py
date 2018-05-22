import useful


def run() -> int:
    closest = (0, float('inf'))

    # If we only look at the 1 x n rectangles, the numbers of possibilities are triangular numbers
    # Since we want two dimensions, we multiply two triangle numbers to get the number of possibilities
    for i in range(1, 1000000):

        # We only check for j's from i onward since the ones before were already checked
        for j in range(i, 1000000):

            # Calculate the number of possibilities for the current rectangle and how far of it is from 2 mil
            current_binomial = useful.binomial(i + 1, 2) * useful.binomial(j + 1, 2)
            diff = abs(current_binomial - 2000000)

            # If the difference is smaller than the previous smallest difference, save the area and the new difference
            if diff < closest[1]:
                closest = (i * j, diff)

            # If the difference is too large and the number of possibilities is above 2 mil, skip to next i
            if diff > 2 * closest[1] and current_binomial > 2e6:
                break

        # If the number of possibilities gets too big, we cancel the loop since the number is only going to get bigger
        if useful.binomial(i + 1, 2) ** 2 > 2 * 1e6 + closest[1]:
            break

    return closest[0]


if __name__ == "__main__":
    from timeit import default_timer as timer

    start = timer()
    print("Solution:", run())
    print("Duration:", timer() - start)
