def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    else:
        list_x = list(str(x))
        list_new = []
        for i in range(len(list_x) - 1, -1, -1):
            list_new.append(list_x[i])

        str1 = [str(i) for i in list_new]
        str2 = ''.join(str1)
        str3 = int(str2)

        if str3 > pow(2, 31) - 1 or str3 < pow(-2, 31):
            return False
        elif str3 == x:
            return True
        else:
            return False

if __name__ == '__main__':
    print(isPalindrome(121))
    print(isPalindrome(-121))
    print(isPalindrome(10))

# Input: x = 121
# Output: true

# Input: x = -121
# Output: false
#
# Input: x = 10
# Output: false


