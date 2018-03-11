stevec = 0
i = 1
nadaljuj = 10
while nadaljuj > 0:
    nadaljuj -= 1
    current_int = 1
    while True:
        powered = current_int ** i
        if len(str(powered)) == i:
            stevec += 1
            nadaljuj = 10
        elif len(str(powered)) > i:
            break
        current_int += 1
    i += 1

print(stevec)
