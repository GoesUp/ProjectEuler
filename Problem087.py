from eulerlib import primes


def run() -> int:
    # Set the upper limit and generate enough primes generate primes
    limit = 5e7
    pra = primes(limit ** .5 + 1)

    # We will be saving suitable numbers here
    below_limit = set()

    # Check all combinations of primes
    for i in pra:
        for j in pra:
            for k in pra:

                # Multiply and add the primes in the needed way
                sum_value = i ** 2 + j ** 3 + k ** 4

                # If the sum exceeds the limit, skip to next j, else save the sum
                if sum_value >= limit:
                    break
                else:
                    below_limit.add(sum_value)

            # Break loops sooner if the numbers are getting too big
            if i ** 2 + j ** 3 + 2 ** 4 >= limit:
                break
        if i ** 2 + 2 ** 3 + 2 ** 4 >= limit:
            break

    return len(below_limit)


if __name__ == "__main__":
    from timeit import default_timer as timer

    start = timer()
    print("Solution:", run())
    print("Duration:", timer() - start)
