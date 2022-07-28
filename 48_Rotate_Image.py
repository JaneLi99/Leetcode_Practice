def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    for i in range(len(matrix[0])):
        new_line = []
        for j in range(len(matrix[0]) - 1, -1, -1):
            new_line.append(matrix[j][i])
        matrix.append(new_line)

    for a in range(len(matrix) // 2):
        matrix.remove(matrix[0])

    return matrix

if __name__ == '__main__':
    print(rotate(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
    print(rotate(matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
