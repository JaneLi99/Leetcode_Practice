def modifyString(s):
    s = list("0" + s + "0")
    for i, l in enumerate(s[:-1]):
        if l == "?":
            for c in "abc":
                if c != s[i - 1] and c != s[i + 1]:
                    s[i] = c
                    break
    return "".join(s[1:-1])

if __name__ == '__main__':
    print(modifyString(s = "?zs"))
    print(modifyString(s = "ubv?w"))