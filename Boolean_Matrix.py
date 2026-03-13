# # Canonical - Technical Exercise - Python OA 2
# A boolean matrix has the parity property when each row and each column has an even sum,
# i.e. contains an even number of bits which are set. Here's a 4×4 matrix which has the parity property:
#
# The sums of the rows are , ,  and . The sums of the columns are , ,  and .
#
# Your job is to write a program that reads in a matrix and checks if it has the parity property.
# If not, your program should check if the parity property can be established by changing only one bit.
# If this is not possible either, the matrix should be classified as corrupt.
#
# The signature of your function should be:
#
# You may implement other functions called by your  function if you wish.
#
# Each input will be a multi-line string where the first line contains the size of the matrix. On the next lines,
# there will be  integers per line. No other integers than  and  will occur in the matrix.
#
# For each input, your function should return a string saying either "OK", "Change bit (y,x)"
# if it can be corrected by flipping one bit (y is the 1-based row number, x is the 1-based column number),
# or "Corrupt" if it is beyond repair.


def solve(matrix_str: str) -> str:
    lines = matrix_str.splitlines()
    n = int(lines[0])
    matrix = [list(map(int, line.split())) for line in lines[1:]]

    invalid_rows = []
    invalid_cols = []

    for i in range(n):
        if sum(matrix[i]) % 2 != 0:
            invalid_rows.append(i)

    for j in range(n):
        col_sum = sum(matrix[i][j] for i in range(n))
        if col_sum % 2 != 0:
            invalid_cols.append(j)

    if len(invalid_rows) == 0 and len(invalid_cols) == 0:
        return "OK"

    if len(invalid_rows) == 1 and len(invalid_cols) == 1:
        row, col = invalid_rows[0], invalid_cols[0]
        matrix[row][col] ^= 1
        new_row_sum = sum(matrix[row]) % 2
        new_col_sum = sum(matrix[i][col] for i in range(n)) % 2
        if new_row_sum == 0 and new_col_sum == 0:
            return f"Change bit ({row + 1},{col + 1})"

    return "Corrupt"

if __name__ == "__main__":
    print(solve(
            """\
            4
            1 0 1 0
            0 0 0 0
            1 1 1 1
            0 1 0 1
            """
        )
    )
    # Output: "OK",

    print(solve(
            """\
            4
            1 0 1 0
            0 0 1 0
            1 1 1 1
            0 1 0 1
            """
        )
    )
    # Output "Change bit (2,3)"