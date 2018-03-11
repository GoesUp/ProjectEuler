low = int(10203040506070809 ** .5)
static = "123456789"
while True:
    if str(low ** 2)[::2] == static:
        print(low * 10)
        break
    low += 2
