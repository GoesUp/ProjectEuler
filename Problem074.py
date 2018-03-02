from math import factorial

seznam = {}

def get_loop_len(n):
    numbers = [n]
    while True:
        if numbers[-1] in seznam:
            numbers = numbers + seznam[numbers[-1]]
            break
        getnew = sum([factorial(int(j)) for j in str(numbers[-1])])
        if getnew in numbers:
            break
        numbers.append(getnew)
    seznam[n] = numbers
    return len(set(numbers))


count = 0
for i in range(1, 10 ** 6):
    if get_loop_len(i) == 60:
        count += 1

print(count)

