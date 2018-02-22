with open("input_data/problem018.txt", "r") as f:
    vnos = list(map(lambda x: list(map(int, x[:-1].split(" "))), f.readlines()))[::-1]

    while len(vnos) > 1:
        for j in range(len(vnos[1])):
            vnos[1][j] = vnos[1][j] + max(vnos[0][j], vnos[0][j + 1])
        vnos = vnos[1:]

    print(vnos[0][0])

# Code identical to problem no. 67
