def addBinary(a, b):
    if a == "1":
        a_dec = 1
    elif a == "0":
        a_dec = 0
    else:
        a_dec = 0
        a_len = len(a) - 1
        for i in range(len(a)):
            a_dec = a_dec + int(a[i]) * pow(2, a_len)
            a_len = a_len - 1

    if b == "1":
        b_dec = 1
    elif b == "0":
        b_dec = 0
    else:
        b_dec = 0
        b_len = len(b) - 1
        for i in range(len(b)):
            b_dec = b_dec + int(b[i]) * pow(2, b_len)
            b_len = b_len - 1

    if a_dec == 0 and b_dec == 0:
        return "0"
    if (a_dec == 0 and b_dec == 1) or (a_dec == 1 and b_dec == 0):
        return "1"

    sum_dec = a_dec + b_dec
    binary_sum_list = []
    while sum_dec != 1:
        binary_sum_list.append(sum_dec % 2)
        sum_dec = sum_dec // 2
    binary_sum_list.append(1)
    binary_sum_list.reverse()
    res = ""
    for i in range(len(binary_sum_list)):
        res = res + str(binary_sum_list[i])
    return res

if __name__ == '__main__':
    print(addBinary(a = "1", b = "111"))
    print(addBinary(a = "1010", b = "1011"))
    print(addBinary(a = "1", b = "0"))
