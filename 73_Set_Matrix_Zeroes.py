def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """

    index_list = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                index_list.append([i, j])

    for index_pattern in index_list:
        for a in range(len(matrix[0])):
            matrix[index_pattern[0]][a] = 0
        for b in range(len(matrix)):
            matrix[b][index_pattern[1]] = 0

    # print(matrix)
    return

if __name__ == '__main__':
    print(setZeroes(matrix = [[1,1,1],[1,0,1],[1,1,1]]))
    print(setZeroes(matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
