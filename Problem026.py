maks = (0, 0)

for i in range(2, 1000):
    skladisce = [(10, 10 // i)]
    while True:
        skladisce.append(((skladisce[-1][0] % i) * 10, ((skladisce[-1][0] % i) * 10) // i))
        if skladisce[-1] in skladisce[:-1]:
            if len(skladisce) - 1 > maks[1]:
                maks = (i, len(skladisce) - 2)
            break

print(maks[0])
