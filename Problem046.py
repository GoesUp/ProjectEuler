from math import sqrt

biggest_possible = 100000
sito = [True for i in range(1, biggest_possible)]
position = 2
primes = []
while position < biggest_possible - 2:
    if sito[position] == True:
        primes.append(position)
        for j in range(position ** 2, len(sito), position):
            sito[j] = False
    position += 1

check = False
count = 9
while not check:
    if count not in primes:
        tempcheck = False
        for w in [a for a in primes if a < count]:
            num1, num2 = sqrt((count - w) / 2), int(sqrt((count - w) / 2))
            if num1 == num2:
                tempcheck = True

        if not tempcheck:
            print(count)
            check = True
            break

    count += 2
