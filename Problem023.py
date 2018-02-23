abundant = []
for i in range(1, 28124):
    divisors = []
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            divisors += [j]
    if sum(divisors) > i:
        abundant.append(i)
combinations = [a + b for a in abundant for b in abundant if a + b < 28124]
print(sum(list(set([w for w in range(1, 28124)]) - set(combinations))))

# GRDO GRDO GRDO
