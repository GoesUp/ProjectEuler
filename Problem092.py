def one_or_eighty_nine(n):
    if n == 1:
        goes_to[n] = 1
        return
    elif n == 89:
        goes_to[n] = 89
        return
    elif n in goes_to:
        return
    sum_of_squares = sum([int(b) ** 2 for b in str(n)])
    if sum_of_squares not in goes_to:
        ćone_or_eighty_nine(sum_of_squares)
    goes_to[n] = goes_to[sum_of_squares]
    return


goes_to = {}
[one_or_eighty_nine(a) for a in range(1, 10 ** 7)]
print(len([True for a in goes_to if goes_to[a] == 89]))
