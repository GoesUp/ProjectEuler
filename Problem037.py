import SieveOfAtkin

primes = SieveOfAtkin.sito(int(1e6))

counter = 0
truncatable = []

while len(truncatable) < 11:
    is_truncatable = True
    temp = primes[counter + 4]
    new_temp = 0
    while is_truncatable and temp > 0:
        temp, new_temp = temp // 10, int(str(temp % 10) + str(new_temp))
        if new_temp % 10 == 0: new_temp = new_temp // 10
        if not (temp in primes and new_temp in primes) and temp != 0:
            is_truncatable = False

    if is_truncatable:
        truncatable.append(primes[counter + 4])

    counter += 1

print(sum(truncatable))
