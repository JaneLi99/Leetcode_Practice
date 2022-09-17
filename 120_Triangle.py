def minimumTotal(triangle):
    if len(triangle) == 1:
        return triangle[0][0]

    for r in range(len(triangle) - 1, 0, -1):
        for c in range(len(triangle[r - 1])):
            triangle[r - 1][c] += min(triangle[r][c], triangle[r][c + 1])
    return triangle[0][0]

if __name__ == '__main__':
    print(minimumTotal(triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]))
    print(minimumTotal(triangle = [[-1],[2,3],[1,-1,-3]]))
    print(minimumTotal(triangle = [[-10]]))