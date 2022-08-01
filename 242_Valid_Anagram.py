def isAnagram(s, t):
    if len(s) != len(t):
        return False

    i = 0
    while i < len(s):
        if s[i] in t:
            t = t.replace(s[i], "", 1)
            s = s.replace(s[i], "", 1)
        else:
            i += 1

    if s == t:
        return True

    return False

if __name__ == '__main__':
    print(isAnagram(s = "anagram", t = "nagaram"))
    print(isAnagram(s = "rat", t = "car"))
    print(isAnagram(s = "aacc", t = "ccac"))
