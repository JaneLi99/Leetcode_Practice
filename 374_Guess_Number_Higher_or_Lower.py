# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num, pick):
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0

def guessNumber(n, pick):
    l, r = 1, n
    while True:
        m = (l + r) // 2
        res = guess(m, pick)
        if res > 0:
            l = m + 1
        elif res < 0:
            r = m - 1
        else:
            return m

if __name__ == '__main__':
    print(guessNumber(n = 10, pick = 6))
    print(guessNumber(n = 1, pick = 1))
    print(guessNumber(n = 2, pick = 1))