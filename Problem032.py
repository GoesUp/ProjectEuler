from Pandigital import generate, check

pandigitals = generate(9, True)
products = []

for i in range(1, 4322):
    for j in range(i, 4322 - i ** 2):
        temp_product = i * j
        concatenated = int(str(temp_product) + str(i) + str(j))
        if len(str(concatenated)) == 9:
            if check(concatenated):
                products += [temp_product]

print(sum(list(set(products))))
