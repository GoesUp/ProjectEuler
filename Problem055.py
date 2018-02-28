def is_lychrel(n, iteration):
    if iteration == 50:
        return True
    if str(n) == str(n)[::-1] and iteration != 0:
        return False
    else:
        return is_lychrel(n + int(str(n)[::-1]), iteration + 1)


print(sum([is_lychrel(i, 0) for i in range(1, 10000)]))
