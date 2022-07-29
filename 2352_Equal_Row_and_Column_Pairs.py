def equalPairs(grid):
    all_col = []
    for i in range(len(grid)):
        each_col = []
        for j in range(len(grid[i])):
            each_col.append(grid[j][i])
        all_col.append(each_col)

    res = 0
    for a in range(len(grid)):
        for b in range(len(all_col)):
            if grid[a] == all_col[b]:
                res = res + 1
    return res

if __name__ == '__main__':
    print(equalPairs(grid = [[3,2,1],[1,7,6],[2,7,7]]))
    # Output: 1
    # Explanation: There is 1 equal row and column pair:
    # - (Row 2, Column 1): [2, 7, 7]

    print(equalPairs(grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))
    # Output: 3
    # Explanation: There are 3 equal row and column pairs:
    # - (Row 0, Column 0): [3, 1, 2, 2]
    # - (Row 2, Column 2): [2, 4, 2, 2]
    # - (Row 3, Column 2): [2, 4, 2, 2]

    print(equalPairs(grid = [[13,13],[13,13]]))
    # Output: 4