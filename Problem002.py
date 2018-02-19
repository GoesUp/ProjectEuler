first, second, vsota_sodih = 1, 2, 2

while max(first, second) < 4 * 10 ** 6:
    first, second = second, first + second
    if second % 2 == 0:
        vsota_sodih += second

print(vsota_sodih)
