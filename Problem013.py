with open("input_data/problem013.txt", "r") as f:
    cifre = list(map(int, f.read().splitlines()))
    print(str(sum(cifre))[:10])
