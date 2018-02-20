below = 2 * 10 ** 6
sito = [True for i in range(1, below+1)]
primes = []
position = 2
while position < below:
    if sito[position] == True:
        for j in range(position, len(sito), position):
            sito[j] = False
        primes += [position]
    position += 1

print(sum(primes))
