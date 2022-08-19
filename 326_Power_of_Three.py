import math

def isPowerOfThree(n):
    if n <= 0:
        return False

    res = math.log(n, 3)
    if res.is_integer() == True:
        return True
    return False

def isPowerOfThree_2(n):
    if n == 0:
        return False
    while n % 3 == 0:
        n = n // 3
        print(n)
    return n == 1

if __name__ == '__main__':
    print(isPowerOfThree(n = 27))
    print(isPowerOfThree(n = 0))
    print(isPowerOfThree(n = 9))

    print(isPowerOfThree_2(n=27))
    print(isPowerOfThree_2(n=0))
    print(isPowerOfThree_2(n=9))