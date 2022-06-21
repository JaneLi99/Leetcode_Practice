def divide(dividend, divisor):
    if (dividend / divisor).is_integer() == True:
        return min(2147483647, max(int(dividend / divisor), -2147483648))
    else:
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            res = dividend // divisor
        elif (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            res = dividend // divisor
            res = res + 1
        return min(2147483647, max(res, -2147483648))


if __name__ == '__main__':
    print(divide(-7, 3))
    print(divide(10, 3))
    print(divide(0, 3))
    print(divide(9, 3))
    print(divide(-9, -3))