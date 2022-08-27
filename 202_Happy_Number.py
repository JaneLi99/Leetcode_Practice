def isHappy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        t = 0
        while n > 0:
            t += (n % 10) ** 2
            n //= 10
        n = t
    return n == 1

if __name__ == '__main__':
    print(isHappy(n = 19))
    print(isHappy(n = 2))