def isMatch(s, p):
    """
    :param s: string
    :param p: string
    :return: bool
    '.' Matches any single character.
    '*' Matches zero or more of the preceding element.
    """
    m = len(s)
    n = len(p)

    dp = [[0 for i in range(n + 1)] for i in range(m + 1)]

    dp [0][0] = 1
    for i in range(1, n + 1):
        if p[i - 1] == "*":
            dp[0][i] = dp[0][i - 2]

    for row in range(1, m + 1):
        for col in range(1, n + 1):
            i = row - 1
            j = col - 1
            if s[i] == p[j] or p[j] == ".":
                dp[row][col] = dp[row - 1][col - 1]
            elif p[j] == "*":
                if dp[row][col - 2] == 1:
                    dp[row][col] = dp[row][col - 2]
                elif s[i] == p[j - 1] or p[j - 1] == ".":
                    dp[row][col] = dp[row - 1][col]

    if dp[m][n] == 1:
        return True

    return False


if __name__ == '__main__':
    print(isMatch(s = "aa", p = "a"))
    print(isMatch(s = "aa", p = "a*"))
    print(isMatch(s = "ab", p = ".*"))
    print(isMatch(s = "ab", p = "ab"))
    print(isMatch(s = "aab", p = "c*a*b"))
