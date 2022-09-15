def numsSameConsecDiff(n, k):
    def dfs(i, path):
        if len(path) == n:
            res.append(int(path))
            return

        pos = k + int(path[i - 1])
        negi = int(path[i - 1]) - k

        if pos in range(0, 10):
            dfs(i + 1, path + str(pos))

        if negi in range(0, 10) and k != 0:
            dfs(i + 1, path + str(negi))

    res = []
    for i in range(1, 10):
        dfs(1, str(i))

    return res

if __name__ == '__main__':
    print(numsSameConsecDiff(n = 3, k = 7))
    # Output: [181, 292, 707, 818, 929]
    print(numsSameConsecDiff(n = 2, k = 1))
    # Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]