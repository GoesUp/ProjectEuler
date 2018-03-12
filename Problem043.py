from Pandigital import generate

vsota = 0
pandigitals = [str(i) for i in generate(9, incl_zero=True) if len(str(i)) == 10]
for j in pandigitals:
    if int(j[1:4]) % 2 == 0:
        if int(j[2:5]) % 3 == 0:
            if int(j[3:6]) % 5 == 0:
                if int(j[4:7]) % 7 == 0:
                    if int(j[5:8]) % 11 == 0:
                        if int(j[6:9]) % 13 == 0:
                            if int(j[7:10]) % 17 == 0:
                                vsota += int(j)

print(vsota)
