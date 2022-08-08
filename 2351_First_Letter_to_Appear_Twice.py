def repeatedCharacter(s):
    for i in range(1, len(s)):
        if s[i] in s[:i]:
            return s[i]

if __name__ == '__main__':
    print(repeatedCharacter(s = "abccbaacz"))
    print(repeatedCharacter(s = "abcdb"))