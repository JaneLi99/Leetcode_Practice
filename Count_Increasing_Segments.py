"""
IBM OA 2

A graph with the adjacent points is represented as an array, yCoordinates, such that the array index represents
the X-coordinate and the corresponding element represents the Y-coordinate. formally, each point (x, y) is
represented as (i, yCoordinates[i]), where 0 <= i <= n.
Find the number of increasing segments that span exactly k consecutive X-coordinates.

Notes
    A segment of the graph is said to be increasing if, for any two points (x1, y1) and (x2, y2), the value of
    (y2 - y1) / (x1, x2) is positive.
    If the value of k is 1, each point is an increasing segment.

Example
yCoordinates = [6, 5, 7, 8, 10]
k = 3
"""

def countIncreasingSegments(yCoordinates, k):
    if len(yCoordinates) < k:
        return 0
    if len(yCoordinates) == 1 and k == 1:
        return 1

    counts = 1
    result = 0
    for i in range(1, len(yCoordinates)):
        if yCoordinates[i] > yCoordinates[i - 1]:
            counts += 1
        else:
            counts = 1

        if counts >= k:
            result += 1

    return result

if __name__ == "__main__":
    print(countIncreasingSegments(yCoordinates = [6, 5, 7, 8, 10], k = 3))