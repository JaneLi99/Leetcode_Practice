def reverse(x):
    """
    :type x: int
    :rtype: int
    """

    if x > 0:
        list_x = list(str(x))
        list_new = []
        for i in range(len(list_x) - 1, -1, -1):
            if list_x[i] == 0:
                list_new.append()
            else:
                list_new.append(list_x[i])
            # print(list_new)
        str1 = [str(i) for i in list_new]
        str2 = ''.join(str1)
        str3 = int(str2)
        # print(str3)
        if str3 > pow(2, 31) - 1 or str3 < pow(-2, 31):
            return 0
        else:
            return str3

    elif x < 0:
        list_x = list(str(x))
        # print(list_x)
        list_x.remove('-')
        # print(list_x)
        list_new = []
        for i in range(len(list_x) - 1, -1, -1):
            if list_x[i] == 0:
                list_new.append()
            else:
                list_new.append(list_x[i])
            # print(list_new)
        str1 = [str(i) for i in list_new]
        str2 = ''.join(str1)
        str3 = int(str2)
        str3 = -str3
        # print(str3)
        if str3 > pow(2, 31) - 1 or str3 < pow(-2, 31):
            return 0
        else:
            return str3

    else:
        return 0

if __name__ == '__main__':
    print(reverse(123))
    print(reverse(-123))
    print(reverse(120))

# Input: x = 123
# Output: 321
#
# Input: x = -123
# Output: -321
#
# Input: x = 120
# Output: 21