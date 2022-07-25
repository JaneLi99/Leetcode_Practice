def searchMatrix(matrix, target):
    for i in range(len(matrix)):
        if target in matrix[i]:
            return True
    return False

if __name__ == '__main__':
    print(searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
    print(searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))