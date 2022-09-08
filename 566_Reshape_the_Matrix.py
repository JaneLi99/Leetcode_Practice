def matrixReshape(mat, r, c):
    mat_list = []
    for i in range(len(mat)):
        mat_list += mat[i]

    if r * c != len(mat_list):
        return mat

    res = []
    j = 0
    while j < len(mat_list):
        res.append(mat_list[j: j + c])
        j = j + c
    return res

if __name__ == '__main__':
    print(matrixReshape(mat = [[1,2],[3,4]], r = 1, c = 4))
    print(matrixReshape(mat = [[1,2],[3,4]], r = 2, c = 4))
    print(matrixReshape(mat = [[1,2],[3,4],[5,6],[7,8]], r = 2, c = 4))