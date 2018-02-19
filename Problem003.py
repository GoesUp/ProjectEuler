factors = []
number = 600851475143

while not number == 1:
    for i in range(2, number + 1):
        if number % i == 0:
            factors += [i]
            number = number // i
            break

print(max(factors))
