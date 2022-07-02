def plusOne(digits):
    str_digit = ""
    for i in range(len(digits)):
        str_digit = str_digit + str(digits[i])

    int_digit = int(str_digit) + 1
    new_str = str(int_digit)
    res = []
    for j in range(len(new_str)):
        res.append(int(new_str[j]))
    return res


if __name__ == '__main__':
    print(plusOne(digits = [1,2,3]))
    print(plusOne(digits = [4,3,2,1]))
    print(plusOne(digits = [9]))