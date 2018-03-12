slovar = {}
for a in range(1, 1001):
    for b in range(a, 1001 - a):
        for c in range(b + 1, 1001 - (a + b)):
            if a ** 2 + b ** 2 == c ** 2:
                if a + b + c in slovar:
                    slovar[a + b + c] = slovar[a + b + c] + 1
                else:
                    slovar[a + b + c] = 1

print(max(slovar, key=slovar.get))
