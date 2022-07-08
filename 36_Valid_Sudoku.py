def isValidSudoku(board):
    for num in range(1, 10):
        num = str(num)
        # check if the number is in the row
        for row in board:
            times = 0
            for i in range(len(row)):
                if num == row[i]:
                    times = times + 1
                if times > 1:
                    print("1 false")
                    return False

        # check if the number is in the column
        for j in range(len(board)):
            times = 0
            for row in board:
                if num == row[j]:
                    times = times + 1
                if times > 1:
                    return False

        # check if the number is in the 3*3 matrix
        for a in range(0, len(board), 3):
            for b in range(0, len(board), 3):
                times = 0
                new_matrix = []
                new_matrix.append(board[a][b:b + 3])
                new_matrix.append(board[a + 1][b:b + 3])
                new_matrix.append(board[a + 2][b:b + 3])
                # print(new_matrix)
                for n in range(len(new_matrix)):
                    if num in new_matrix[n]:
                        times = times + 1
                    if times > 1:
                        return False
    return True

if __name__ == '__main__':
    print(isValidSudoku(board =
                        [["5","3",".",".","7",".",".",".","."]
                        ,["6",".",".","1","9","5",".",".","."]
                        ,[".","9","8",".",".",".",".","6","."]
                        ,["8",".",".",".","6",".",".",".","3"]
                        ,["4",".",".","8",".","3",".",".","1"]
                        ,["7",".",".",".","2",".",".",".","6"]
                        ,[".","6",".",".",".",".","2","8","."]
                        ,[".",".",".","4","1","9",".",".","5"]
                        ,[".",".",".",".","8",".",".","7","9"]]))
    print(isValidSudoku(board =
                        [["8", "3", ".", ".", "7", ".", ".", ".", "."]
                        ,["6", ".", ".", "1", "9", "5", ".", ".", "."]
                        ,[".", "9", "8", ".", ".", ".", ".", "6", "."]
                        ,["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                        ,["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                        ,["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                        ,[".", "6", ".", ".", ".", ".", "2", "8", "."]
                        ,[".", ".", ".", "4", "1", "9", ".", ".", "5"]
                        ,[".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
    print(isValidSudoku(board =
                        [[".","4",".",".",".",".",".",".","."]
                        ,[".",".","4",".",".",".",".",".","."]
                        ,[".",".",".","1",".",".","7",".","."]
                        ,[".",".",".",".",".",".",".",".","."]
                        ,[".",".",".","3",".",".",".","6","."]
                        ,[".",".",".",".",".","6",".","9","."]
                        ,[".",".",".",".","1",".",".",".","."]
                        ,[".",".",".",".",".",".","2",".","."]
                        ,[".",".",".","8",".",".",".",".","."]]))