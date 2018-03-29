from Pandigital import generate

pandigits = set(generate(9, True, False))
fib1, fib2 = 1, 1
count = 2
while True:
    fib1, fib2 = fib2, fib1 + fib2
    count += 1
    if fib2 % 10 ** 9 in pandigits:
        if int(str(fib2)[::-1]) % 10 ** 9 in pandigits:
            print(count)
            break
