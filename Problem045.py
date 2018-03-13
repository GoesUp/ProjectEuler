hexa = lambda x: int(x * (2 * x - 1))
penta = lambda x: x * (3 * x - 1) // 2
hexa_list, penta_list = [], []

for i in range(2, 10 ** 5):
    hexa_list.append(hexa(i))
    penta_list.append(penta(i))

penta_list.remove(40755)
print(list(set(hexa_list).intersection(penta_list))[0])
