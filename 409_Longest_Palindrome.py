def longestPalindrome(s):
    if len(s) == 1:
        return 1
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    v = list(d.values())
    s1 = 0
    for i in range(len(v)):
        if v[i] % 2 != 0 and v[i] != 1:
            s1 = s1 + (v[i] - 1)
        elif v[i] % 2 == 0:
            s1 += v[i]

    if len(s) > s1:
        return s1 + 1
    else:
        return s1

if __name__ == '__main__':
    print(longestPalindrome(s = "abccccdd"))
    print(longestPalindrome(s = "a"))
    print(longestPalindrome(s = "bb"))