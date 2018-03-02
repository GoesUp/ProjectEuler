biggest_possible = 10000
sito = [True for i in range(1, biggest_possible)]
position = 2
primes = []
while position < biggest_possible - 2:
    if sito[position] == True:
        if len(str(position)) == 4:
            primes.append(position)
        for p in range(position ** 2, len(sito), position):
            sito[p] = False
    position += 1

for i in range(len(primes)):
    for j in range(i + 1, len(primes)):
        first, second = primes[i], primes[j]
        set1, set2 = [set(str(o)) for o in [first, second]]
        if set1 == set2:
            for k in range(j + 1, len(primes)):
                third = primes[k]
                set3 = set(str(third))
                if (set1 == set3) and (third - second == second - first) and (first != 1487):
                    print(str(first) + str(second) + str(third))
                    break
