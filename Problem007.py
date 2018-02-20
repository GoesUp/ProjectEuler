import math

prime_quantity = 10001
biggest_possible = int(prime_quantity * math.log(prime_quantity) * 1.5)
sito = [True for i in range(1, biggest_possible)]
count = 0
position = 2
while not count == prime_quantity:
    if sito[position] == True:
        for j in range(position, len(sito), position):
            sito[j] = False
        count += 1
    position += 1

print(position-1)
