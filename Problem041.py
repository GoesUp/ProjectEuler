from Pandigital import generate
from SieveOfAtkin import sito

upto = 987654321
primes = sito(int(upto ** (1 / 2)))[2:]
pandigitals = sorted(generate(9))[::-1]
while True:
    temp = pandigitals.pop(0)
    is_prime = True
    if temp % 2 != 0 and temp % 3 != 0:
        for i in primes:
            if temp % i == 0:
                is_prime = False
                break
    else:
        is_prime = False
    if is_prime:
        print(temp)
        break
