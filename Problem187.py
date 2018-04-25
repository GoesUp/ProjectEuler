from eulerlib import primes

def run() -> int:
    pra = primes(5e7)
    valid = set()
    for i in range(len(pra)):
        for j in range(i, len(pra)):
            product = pra[i] * pra[j]
            if product < 1e8:
                valid.add(product)
            else:
                break

    return len(valid)


if __name__ == "__main__":
    from timeit import default_timer as timer

    start = timer()
    print("Solution:", run())
    print("Duration:", timer() - start)

