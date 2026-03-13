# A mountaineer is studying a mountain range with several peaks of different heights.
# The peaks are arranged in a line, numbered from 0 onwards.
#
# Due to an optical illusion, the mountaineer can only compare peaks that are at least a certain number of positions apart.
#
# Given:
# an array heights representing the heights of the peaks (in meters)
# an integer viewingGap representing the minimum distance between two peaks that can be compared
# Find the most similar pair of peaks, defined as the pair with the smallest height difference that satisfies the distance constraint.
# In other words, compute:
# min |heights[a] - heights[b]|
# such that
# |a - b| ≥ viewingGap
# Return this minimum height difference.
#
# Example 1
# heights = [1, 5, 4, 10, 9]
# viewingGap = 3
# Output:
# 4

# Example 2
# heights = [3, 10, 5, 8]
# viewingGap = 1
# Output:
# 2

from typing import List


def solution(heights: List[int], viewingGap: int) -> int:
    """
    Return the minimum |heights[a] - heights[b]| where |a - b| >= viewingGap
    """

    n = len(heights)
    min_diff = float("inf")

    for i in range(n):
        for j in range(i + viewingGap, n):
            diff = abs(heights[i] - heights[j])
            min_diff = min(min_diff, diff)

    return min_diff


def main():
    # Example 1
    heights1 = [1, 5, 4, 10, 9]
    viewingGap1 = 3

    print("Example 1 result:", solution(heights1, viewingGap1))
    # Example 2
    heights2 = [3, 10, 5, 8]
    viewingGap2 = 1
    print("Example 2 result:", solution(heights2, viewingGap2))


if __name__ == "__main__":
    main()