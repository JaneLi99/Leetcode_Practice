def binaryGap(n):
    binary_n = ""
    while n != 0:
        binary_n += str(n % 2)
        n = n // 2
    binary_n = binary_n[::-1]
    # print(binary_N)

    res = 0
    idx = 0
    for i, num in enumerate(binary_n):
        if num == "1":
            res = max(i - idx - 1, res)
            idx = i
    return res

if __name__ == '__main__':
    print(binaryGap(529))
    print(binaryGap(20))
    print(binaryGap(15))
    print(binaryGap(32))
