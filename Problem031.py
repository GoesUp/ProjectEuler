count = 0
for i in range(201):
    for j in range(201 - i * 1):
        for k in range(201 - (i * 1 + j * 2)):
            for l in range(201 - (i * 1 + j * 2 + k * 5)):
                for m in range(201 - (i * 1 + j * 2 + k * 5 + l * 10)):
                    for n in range(201 - (i * 1 + j * 2 + k * 5 + l * 10 + m * 20)):
                        for o in range(201 - (i * 1 + j * 2 + k * 5 + l * 10 + m * 20 + n * 50)):
                            for p in range(201 - (i * 1 + j * 2 + k * 5 + l * 10 + m * 20 + n * 50 + o * 100)):
                                if i * 1 + j * 2 + k * 5 + l * 10 + m * 20 + n * 50 + o * 100 + p * 200 == 200:
                                    count += 1

print(count)
