from SieveOfAtkin import sito

primes = sito(10 ** 6)

final = 1
counter = 0
while final * primes[counter] < 1e6:  # https://en.wikipedia.org/wiki/Euler%27s_totient_function
    final *= primes[counter]  # we transform the functions - turns out, we have to multiply primes till we reach 1 mil
    counter += 1
print(final)
