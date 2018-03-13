from SieveOfAtkin import sito

primes = sito(int(1e6))
biggest = (0, 0)
for i in range(len(primes)):
    vsota = primes[i]
    for j in range(i + 1, len(primes) - i):
        vsota += primes[j]
        if j-i > biggest[1]:
            if vsota in primes and j - i > biggest[1]:
                biggest = (vsota, j - i)
        if vsota > 1e6:
                break

print(biggest[0])
