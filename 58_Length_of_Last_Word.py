def lengthOfLastWord(s):
    split_s = s.split(" ")

    n = len(split_s) - 1
    while n >= 0:
        if len(split_s[n]) != 0:
            return len(split_s[n])
        n = n - 1

if __name__ == '__main__':
    print(lengthOfLastWord(s = "Hello World"))
    print(lengthOfLastWord(s = "   fly me   to   the moon  "))
    print(lengthOfLastWord(s = "luffy is still joyboy"))