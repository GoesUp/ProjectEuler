palindromi = []

for i in reversed(range(100, 1000)):
    for j in reversed(range(100, 1000)):
        current = i * j
        if str(current) == str(current)[::-1]:
            palindromi += [current]

print(max(palindromi))
