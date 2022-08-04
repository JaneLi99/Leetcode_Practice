def mirrorReflection(p, q):
    m = n = 1
    while p * m != q * n:
        n += 1
        m = q * n // p

    if n % 2 == 0:
        return 2
    if m % 2:
        return 1
    return 0

if __name__ == '__main__':
    print(mirrorReflection(p = 2, q = 1))
    print(mirrorReflection(p = 3, q = 1))