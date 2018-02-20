found = False

for i in range(1, 999):
    if not found:
        for j in range(1, i):
            for k in range(1, j):
                if (i + j + k == 1000) and (k ** 2 + j ** 2 == i ** 2):
                    print(i * j * k)
                    found = True
                    break

# Bruteforce, yuck
