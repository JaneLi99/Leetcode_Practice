def convert(s: str, numRows: int):
    if numRows == 1 or numRows >= len(s):
        return s

    result = ["" for _ in range(numRows)]
    row = 0
    step = 1
    for letter in s:
        result[row] = result[row] + letter
        if row == 0:
            step = 1
        elif row == numRows - 1:
            step = -1
        row = row + step

    result = ''.join(result)
    return result

if __name__ == '__main__':
    print(convert("apple", 3))