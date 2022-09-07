def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1, 1]

    res = []
    res.append([1])
    res.append([1, 1])
    for i in range(2, rowIndex + 1):
        j = 0
        new_res = []
        new_res.append(1)
        while j < len(res[i - 1]) - 1:
            new_res.append(res[i - 1][j] + res[i - 1][j + 1])
            j = j + 1
        new_res.append(1)
        res.append(new_res)
    return res[-1]

if __name__ == '__main__':
    print(getRow(rowIndex = 3))
    print(getRow(rowIndex = 0))
    print(getRow(rowIndex = 1))
    print(getRow(rowIndex = 5))