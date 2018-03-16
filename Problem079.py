from Pandigital import generate
import re

with open("input_data/problem079.txt", "r") as f:
    numbers = sorted(list(set(f.read().splitlines())))
    missing = sorted(list(set([i for i in range(10)]) - set([int(j) for j in "".join(numbers)])))
    pandigit = list(set(map(str, generate(9, False, True, missing))))
    for i in numbers:
        pandigit = [a for b in [re.findall("^.*%s.*%s.*%s.*$" % (i[0], i[1], i[2]), j) for j in pandigit] for a in b]
    print(int(min(pandigit, key=len)))
