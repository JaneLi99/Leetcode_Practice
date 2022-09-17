def sumZero(n):
    res = []

    half = n // 2
    for i in range(1, half + 1):
        res.append(i)
        res.append(i * -1)

    if n % 2 == 1:
        res.append(0)

    return res

print(sumZero(n = 5))
print(sumZero(n = 3))
print(sumZero(n = 1))