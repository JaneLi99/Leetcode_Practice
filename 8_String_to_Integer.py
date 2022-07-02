def myAtoi(s):
    max_int = 2 ** 31 - 1
    min_int = - 2 ** 31

    res = 0
    negative = 1
    i = 0

    while i < len(s) and s[i] == " ":
        i = i + 1

    if i < len(s) and s[i] == "-":
        negative = -1
        i = i + 1
    elif i < len(s) and s[i] == "+":
        i = i + 1

    check_numbers = set("0123456789")
    while i < len(s) and s[i] in check_numbers:
        res = res * 10 + int(s[i])
        i = i + 1

    res = res * negative

    if res < 0:
        return max(res, min_int)
    return min(res,max_int)

if __name__ == '__main__':
    print(myAtoi("42"))
    print(myAtoi("    -42"))
    print(myAtoi("4193 with words"))
    print(myAtoi("eferf99-2"))