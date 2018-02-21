num = 2 ** 1000

def sestejStevke(n):
    totalSum = 0
    while n > 0:
        totalSum, n = totalSum + n % 10, n // 10
    return totalSum

print(sestejStevke(num))