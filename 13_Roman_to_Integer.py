def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    list_s = "".join(s)
    integer_s = []
    for i in range(len(list_s)):
        if list_s[i] == 'I':
            integer_s.append(1)
        elif list_s[i] == 'V':
            integer_s.append(5)
        elif list_s[i] == 'X':
            integer_s.append(10)
        elif list_s[i] == 'L':
            integer_s.append(50)
        elif list_s[i] == 'C':
            integer_s.append(100)
        elif list_s[i] == 'D':
            integer_s.append(500)
        elif list_s[i] == 'M':
            integer_s.append(1000)
    #print(integer_s)

    integer_number = 0
    j = len(integer_s) - 1
    while j >= 0:
        if len(integer_s) == 1:
            integer_number = integer_s[j-1]
            break
        else:
            if j == 0:
                integer_number = integer_number + integer_s[j]
                # print('The', j, 'iteration', integer_number)
                break
            else:
                if integer_s[j] > integer_s[j - 1]:
                    integer_number = integer_number + integer_s[j] - integer_s[j - 1]
                    # print('The', j, 'iteration', integer_number)
                    j = j - 2
                else:
                    integer_number = integer_number + integer_s[j]
                    # print('The', j, 'iteration', integer_number)
                    j = j - 1

    # print('The final integer number is', integer_number)
    return integer_number

if __name__ == '__main__':
    print(romanToInt("III"))
    print(romanToInt("LVIII"))
    print(romanToInt("MCMXCIV"))

# Input: s = "III"
# Output: 3
#
# Input: s = "LVIII"
# Output: 58
#
# Input: s = "MCMXCIV"
# Output: 1994