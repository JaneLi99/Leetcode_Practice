def countNegatives(grid):
    num = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] < 0:
                num += 1
    return num


if __name__ == '__main__':
    print(countNegatives(grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
    print(countNegatives(grid = [[3,2],[1,0]]))
