with open("input_data/problem022.txt", "r") as f:
    imena = sorted([i[1:-1] for i in f.read().split(",")])
    print(sum([(j + 1) * (sum([ord(k) - 64 for k in imena[j]])) for j in range(len(imena))]))
