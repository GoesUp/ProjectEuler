from Pandigital import generate

pandigitals = generate(9)

najvecje = 0

for i in range(1, 9999):
    w = 1
    produkti = ""
    while True:
        produkti += str(i * w)
        w += 1
        if len(produkti) > 9:
            break
        elif len(produkti) == 9:
            produkti = int(produkti)
            if produkti in pandigitals and produkti > najvecje:
                najvecje = produkti
            break

print(najvecje)