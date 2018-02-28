primes = []

def preveri_pratstevilo(n):
    if (n < 2) or (n % 2 == 0):
        return False
    elif n in primes:
        return True
    else:
        for i in range(2, (n // 2) + 1):
            if n % i == 0:
                return False
        primes.append(n)
        return True

najvecji_b, najvecji_a = 0, 0
najvecja_kolicina = 0

for j in range(-1000, 1000):
    for k in range(-1000,1001):
        count = 0
        while preveri_pratstevilo(count ** 2 + count * j + k):
            count += 1
        if count > najvecja_kolicina:
            najvecja_kolicina = count
            najvecji_a = j
            najvecji_b = k

print(najvecji_b * najvecji_a)