def convertToTitle(columnNumber):
    res = ""
    while columnNumber > 0:
        c = chr(ord('A') + (columnNumber - 1) % 26)
        res = c + res
        columnNumber = (columnNumber - 1) // 26
    return res

if __name__ == '__main__':
    print(convertToTitle(columnNumber = 1))
    print(convertToTitle(columnNumber = 28))
    print(convertToTitle(columnNumber = 701))