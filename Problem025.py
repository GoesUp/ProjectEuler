initial = [1, 1]
while len(str(initial[-1])) < 1000:
    initial.append(initial[-2] + initial[-1])
print(len(initial))
