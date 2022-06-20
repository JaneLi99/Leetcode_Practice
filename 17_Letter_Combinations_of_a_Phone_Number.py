def letterCombinations(digits):
    lib = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    if digits == "":
        return []

    res = [""]
    for d in digits:
        tmp = []
        for v in lib[d]:
            for r in res:
                tmp.append(r+v)
        res = tmp

    # print(res)
    return res


if __name__ == '__main__':
    letterCombinations("732")
    # letterCombinations("")
    # letterCombinations("2")
    # letterCombinations("56")