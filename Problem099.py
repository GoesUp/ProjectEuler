from math import log

with open("input_data/problem099.txt", "r") as f:
    vnos = [[int(b) for b in (a[:-1]).split(",")] for a in f.readlines()]
    max, count = 0, 0
    for i in range(len(vnos)):
        x, y = vnos[i]
        temp = y * log(x)
        if temp > max:
            max = temp
            count = i + 1

    print(count)
