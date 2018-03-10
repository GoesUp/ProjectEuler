import functools

with open("input_data/problem011.txt", "r") as f:
    grid = [[int(k) for k in i] for i in [j.split() for j in f.readlines()]]

    kombinacije = []

    # kombinacije za vodoravno in navpično
    for w in range(len(grid)):
        for z in range(17):
            kombinacije += [[grid[w][z + x] for x in range(4)]]
            kombinacije += [[grid[z + x][w] for x in range(4)]]

    # kombinacije za diagonalno
    for a in range(len(grid) - 4):
        for b in range(len(grid) - 4):
            kombinacije += [[grid[a + x][b + x] for x in range(4)]]
            kombinacije += [[grid[4 + a - x][b + x] for x in range(4)]]

    print(max([functools.reduce(lambda lbd1, lbd2: lbd1 * lbd2, z) for z in kombinacije]))
