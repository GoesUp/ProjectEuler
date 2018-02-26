triangle_nums = [(n * (n + 1)) // 2 for n in range(1, 1000)]
with open("input_data/problem042.txt", "r") as f:
    words = [i[1:-1] for i in f.read().split(",")]
    print(sum(True for i in words if sum(ord(k) - 64 for k in i) in triangle_nums))
