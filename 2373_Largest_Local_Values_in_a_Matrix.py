def largestLocal(grid):
    n = len(grid)

    new_list = []
    i = 0
    while i <= n - 3:
        j = 0
        while j <= n - 3:
            new_list.append(grid[i][j : j + 3] + grid[i + 1][j : j + 3] + grid[i + 2][j : j + 3])
            j = j + 1
        i = i + 1
    # print(new_list)

    max_list = []
    for i in range(len(new_list)):
        max_num = max(new_list[i])
        max_list.append(max_num)
    # print(max_list)

    new_len = n - 2
    res = []
    for a in range(0, len(max_list), new_len):
        res_ele = max_list[a : a + new_len]
        res.append(res_ele)
    return res

if __name__ == '__main__':
    print(largestLocal(grid = [[9,9,8,1],
                               [5,6,2,6],
                               [8,2,6,4],
                               [6,2,2,2]]))
    # Output: [[9,9],[8,6]]

    print(largestLocal(grid = [[1,1,1,1,1],
                               [1,1,1,1,1],
                               [1,1,2,1,1],
                               [1,1,1,1,1],
                               [1,1,1,1,1]]))
    # Output: [[2, 2, 2], [2, 2, 2], [2, 2, 2]]