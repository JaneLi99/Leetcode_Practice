def minFallingPathSum(matrix):
    for i in range(1, len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] += min(matrix[i - 1][max(j - 1, 0):j + 2])
    return min(matrix[-1])

if __name__ == '__main__':
    print(minFallingPathSum(matrix = [[2,1,3],[6,5,4],[7,8,9]]))
    print(minFallingPathSum(matrix = [[-19,57],[-40,-5]]))