import math

def isPowerOfFour(n):
    if n <= 0:
        return False
    res = math.log(n, 4)
    return res.is_integer()

if __name__ == '__main__':
    print(isPowerOfFour(n = 16))
    print(isPowerOfFour(n = 5))
    print(isPowerOfFour(n = 2))