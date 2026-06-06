# Problem:
# Count Regular and Nearly Regular CrossesGiven an m * n integer matrix grid,
# a cross is defined by the union of all elements in the ith row and the jth column, intersecting at the cell (i, j).
    # A cross is Regular if all elements in the ith row and all elements in the jth column are equal to the same value V.
    # A cross is Nearly Regular if all elements in the ith row (excluding the intersection(i, j))
    # and all elements in the jth column (excluding the intersection (i, j) are equal to the same value V.
    # Note that in a Nearly Regular cross, the value at (i, j) does not have to equal V.
# Return the total count of Nearly Regular crosses in the matrix. (Note: By definition, all Regular crosses are also Nearly Regular crosses.)

# Regular Cross
# A cross is regular if all elements in the cross are equal.
# Example:
# 2 2 2
# 2 2 2
# 2 2 2
# If the center is (1,1), the row and column elements are all 2.

# Nearly Regular Cross
# A cross is nearly regular if:
# All elements in the cross are equal except possibly the intersection element (r,c).
# Example:
# 2 2 2
# 2 9 2
# 2 2 2
# Row and column values are all 2, except the center 9.
# This is a nearly regular cross.


def countCrosses(matrix):
    if not matrix or not matrix[0]:
        return 0

    m, n = len(matrix), len(matrix[0])
    count = 0

    for r in range(m):
        for c in range(n):
            center = matrix[r][c]

            # Build all values in the cross except the center
            others = []

            for j in range(n):
                if j != c:
                    others.append(matrix[r][j])

            for i in range(m):
                if i != r:
                    others.append(matrix[i][c])

            # Regular: all values in cross equal to center
            if all(x == center for x in others):
                count += 1
                continue

            # Nearly regular: all non-center values equal to each other
            if others:
                first = others[0]
                if all(x == first for x in others):
                    count += 1

    return count


def main():
    test_cases = [
        [
            [2, 2, 2],
            [2, 2, 2],
            [2, 2, 2]
        ],
        [
            [2, 2, 2],
            [2, 9, 2],
            [2, 2, 2]
        ],
        [
            [1, 2, 1],
            [2, 3, 2],
            [1, 2, 1]
        ],
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    ]

    for i, matrix in enumerate(test_cases, 1):
        print(f"Test Case {i}")
        for row in matrix:
            print(row)

        result = countCrosses(matrix)  # your function
        print("Result:", result)
        print()


if __name__ == "__main__":
    main()