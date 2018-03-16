# Setting the diagonal direction functions:
u_r = lambda x: 4 * (x ** 2) - 10 * x + 7  # OEIS: A054554
u_l = lambda x: 4 * ((x - 1) ** 2) + 1  # OEIS: A053755
d_l = lambda x: 4 * (x ** 2) - 6 * x + 3  # OEIS: A054569
d_r = lambda x: (2 * (x - 1) + 1) ** 2  # OEIS: A016754
is_prime = lambda y: y % 2 == 1 and len(list(filter(lambda x: y % x == 0, range(3, int(y ** 0.5) + 1, 2)))) == 0


def get_more_diagonals_and_check_if_they_are_prime(n: int) -> int:
    # we needn't check the down-right diagonal - it's always a square number
    return sum([is_prime(diagonal(n)) for diagonal in [u_r, u_l, d_l]])


counter = (0, 1)
current = 2
while True:
    counter = (counter[0] + get_more_diagonals_and_check_if_they_are_prime(current), counter[1] + 4)
    if counter[0] / counter[1] < 0.1:
        break
    current += 1

print(current * 2 - 1)
