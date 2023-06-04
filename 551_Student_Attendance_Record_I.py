def checkRecord(s):
    A_freq = 0
    for i in range(len(s)):
        print(i, s[i:i+3])
        if s[i] == "A":
            A_freq += 1
        elif i < len(s) - 3 and s[i: i + 3] == "LLL":
            return False

    if A_freq >= 2:
        return False

    return True


class Solution:
    def checkRecord(self, s):
        return

if __name__ == '__main__':
    print(checkRecord(s = "PPALLP"))
    print(checkRecord(s = "PPALLL"))
