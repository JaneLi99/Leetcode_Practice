# Bubble Explosion Board Problem
# Imagine you are given a board of cells, each containing a bubble of a specific color.
# Neighboring cells are defined as adjacent cells sharing a side (same row or column).
# For a given cell, its neighbors are the cells up, down, left, and right of it.
#
# Your task is to perform a bubble explosion on the board following these rules:
# 1. A bubble within any cell is eligible to explode if it has the same color as bubbles in at least 2 neighboring cells.
# 2. When a bubble is eligible: The bubble itself and its neighboring bubbles of the same color are marked for explosion.
# 3. All marked bubbles explode at the same time.
#   1) Exploded bubbles are removed from the board.
#   2) Removed cells become empty.
# 4. After the explosion: All bubbles above empty cells fall down to fill the empty spaces (gravity effect).

# Input
# You are given an initial board: bubbles: int[][]
# A 2D grid of integers
# Each integer represents a bubble color
# Empty cells should be represented as 0

# Output
# Return the board state after one bubble explosion, where:
# Exploded bubbles are removed
# Remaining bubbles fall down
# Empty cells are represented with 0

# Constraints
# You are not required to produce the most optimal solution, but the time complexity should not be worse than: O(rows² × cols²)

from typing import List

def bubble_explosion(bubbles: List[List[int]]) -> List[List[int]]:
    # find which bubble will explode:
    rows = len(bubbles)
    cols = len(bubbles[0])

    explode = set()

    for row in range(rows):
        for column in range(cols):
            if bubbles[row][column] == 0:
                continue
            color = bubbles[row][column]
            same_neighbors = []
            if row > 0 and bubbles[row - 1][column] == color:
                same_neighbors.append((row - 1, column))
            if row < rows - 1 and bubbles[row + 1][column] == color:
                same_neighbors.append((row + 1, column))
            if column > 0 and bubbles[row][column - 1] == color:
                same_neighbors.append((row, column - 1))
            if column < cols - 1 and bubbles[row][column + 1] == color:
                same_neighbors.append((row, column + 1))
            if len(same_neighbors) >= 2:
                explode.add((row, column))
                for n in same_neighbors:
                    explode.add(n)

    # print(explode)
    for r, c in explode:
        bubbles[r][c] = 0

    for c in range(cols):
        write = rows - 1
        for r in range(rows - 1, -1, -1):
            if bubbles[r][c] != 0:
                bubbles[write][c] = bubbles[r][c]
                if write != r:
                    bubbles[r][c] = 0
                write -= 1

    return bubbles


def print_board(board: List[List[int]]):
    for row in board:
        print(row)
    print()

def main():

    board = [
        [1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 2, 0],
        [3, 0, 2, 2, 2],
        [0, 3, 0, 2, 0]
    ]

    print("Original Board:")
    print_board(board)

    result = bubble_explosion(board)

    print("After Explosion:")
    print_board(result)

if __name__ == "__main__":
    board = [
        [1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 2, 0],
        [3, 0, 2, 2, 2],
        [0, 3, 0, 2, 0]
    ]

    print(bubble_explosion(board))
    # main()