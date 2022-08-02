import math

def isPowerOfTwo(n):
    if n <= 0:
        return False
    res = math.log2(n)
    return res.is_integer()

if __name__ == '__main__':
    print(isPowerOfTwo(n = 1))
    print(isPowerOfTwo(n = 16))
    print(isPowerOfTwo(n = 3))
    print(isPowerOfTwo(n = 0))