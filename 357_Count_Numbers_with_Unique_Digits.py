import math

def countNumbersWithUniqueDigits(n):
    result = 1
    for i in range(1, n + 1):
        result += 9 * math.perm(9, i - 1)
    return result

if __name__ == '__main__':
    print(countNumbersWithUniqueDigits(n = 2))
    print(countNumbersWithUniqueDigits(n = 0))
    print(countNumbersWithUniqueDigits(n = 4))