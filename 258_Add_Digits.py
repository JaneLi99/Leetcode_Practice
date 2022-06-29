def addDigits(num):
    num_string = str(num)
    if len(num_string) == 1:
        return num

    while len(num_string) > 1:
        res = 0
        for i in range(len(num_string)):
            res = res + int(num_string[i])
        num_string = str(res)

    return res


if __name__ == '__main__':
    print(addDigits(num = 38))
    print(addDigits(num = 0))
