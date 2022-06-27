def countAndSay(n):
    if n == 1:
        return "1"
    if n == 2:
        return "11"

    s = "11"
    for j in range(3, n + 1):
        s += "K"
        m = len(s)
        i = 1
        temp = ""
        count = 1
        while i < m:
            if s[i] != s[i - 1]:
                temp += str(count + 0)
                temp += s[i - 1]
                count = 1
            else:
                count += 1
            i += 1
        s = temp

    return s


if __name__ == '__main__':
    print(countAndSay(1))
    print(countAndSay(4))
