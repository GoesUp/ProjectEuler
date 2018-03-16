import functools

with open("input_data/problem008.txt", "r") as f:
    max = 0
    number = "".join(f.read().splitlines())
    for i in range(1000 - 12):
        trinajst_stevk = [int(j) for j in number[i:i + 13]]
        zmnozek = functools.reduce(lambda x, y: x * y, trinajst_stevk)
        if zmnozek > max:
            max = zmnozek

    print(max)
