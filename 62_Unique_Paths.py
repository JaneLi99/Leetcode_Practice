def uniquePaths(m, n):
    row = [1] * n
    for i in range(m - 1):
        new_row = [1] * n
        for j in range(n - 2, -1, -1):
            new_row[j] = new_row[j + 1] + row[j]
        row = new_row
    return row[0]

# O(n * m) O(n)

if __name__ == '__main__':
    print(uniquePaths(m = 3, n = 7))
    print(uniquePaths(m = 3, n = 2))