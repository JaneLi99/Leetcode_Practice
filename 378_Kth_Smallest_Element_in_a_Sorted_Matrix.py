def kthSmallest(matrix, k):
    res = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            res.append(matrix[j][i])
    res.sort()
    return res[k - 1]

if __name__ == '__main__':
    print(kthSmallest(matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8))
    print(kthSmallest(matrix = [[-5]], k = 1))