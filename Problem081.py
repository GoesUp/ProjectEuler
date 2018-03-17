with open("input_data/problem081.txt", "r") as f:
    matrika = [[int(j) for j in i.split(",")] for i in f.readlines()]
    options = []
    for a in range(2 * len(matrika) - 1):
        current_opt = []
        for x in range(a + 1):
            for y in range(a + 1):
                if x + y == a and x < len(matrika) and y < len(matrika):
                    current_opt.append((x, y))
        options.append(current_opt)
    polja = {}
    for b in range(len(options)):
        for c, d in options[b]:
            polja[(c, d)] = matrika[c][d]
    for e in options[1:]:
        for g, h in e:
            candidates = []
            if g != 0:
                candidates.append((g - 1, h))
            if h != 0:
                candidates.append((g, h - 1))
            min_value = min([polja[o] for o in candidates])
            polja[(g, h)] += min_value

    print(polja[(len(matrika) - 1, len(matrika) - 1)])
