from fractions import Fraction


def run() -> int:
    fraction_parts = [2]
    n = 1
    while len(fraction_parts) < 100:
        fraction_parts.append(1)
        fraction_parts.append(n * 2)
        fraction_parts.append(1)
        n += 1
    fraction_parts = fraction_parts[:100]

    def build_fraction() -> Fraction:
        ulomek = Fraction(fraction_parts.pop(), 1)
        while len(fraction_parts) > 0:
            ulomek = fraction_parts.pop() + Fraction(1, ulomek)
        return ulomek

    final_fraction = build_fraction()
    return sum(int(i) for i in str(final_fraction.numerator))


if __name__ == "__main__":
    from timeit import default_timer as timer

    start = timer()
    print("Solution:", run())
    print("Duration:", timer() - start)
