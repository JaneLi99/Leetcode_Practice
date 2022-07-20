def generate(numRows):
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1, 1]]

    res = []
    res.append([1])
    res.append([1, 1])
    for i in range(2, numRows):
        j = 0
        new_res = []
        new_res.append(1)
        while j < len(res[i - 1]) - 1:
            new_res.append(res[i - 1][j] + res[i - 1][j + 1])
            j = j + 1
        new_res.append(1)
        res.append(new_res)
    return res

if __name__ == '__main__':
    print(generate(numRows = 5))
    print(generate(numRows = 7))
    print(generate(numRows = 1))