def intToRoman(num):
    res = ""
    symlist = [
        ["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10],
        ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], ["CD", 400],
        ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]
    ]

    for sym, val in reversed(symlist):
        if num // val:
            count = num //val
            res = res + count * sym
            num = num % val
    return res

if __name__ == '__main__':
    print(intToRoman(3))
    print(intToRoman(58))
    print(intToRoman(2994))

# Input: num = 3
# Output: "III"
#
# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
#
# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.