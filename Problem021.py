delitelji = {1: 1}
sol = []


def najdiDelitelje(n):
    return sum([j for j in range(1, (n // 2) + 1) if n % j == 0])


for i in range(2, 10000):
    delitelji[i] = najdiDelitelje(i)

for k in range(2, 10000):
    if delitelji[k] < 10000:
        if (delitelji[delitelji[k]] == k) and (delitelji[k] != k):
            sol.append(k)

print(sum(list(set(sol))))
