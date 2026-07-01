# Question:
# Given a list of intervals where each interval is [start, end], merge all overlapping intervals and return the result.
# Two intervals overlap if one starts before or exactly when the other ends.

# Input:  [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: [1,3] and [2,6] overlap → merge to [1,6]
#
# Input:  [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: [1,4] and [4,5] touch at 4 → merge to [1,5]
#
# Input:  [[1,4],[2,3]]
# Output: [[1,4]]
# Explanation: [2,3] is fully inside [1,4]

def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda k: k[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        last_end = merged[-1][1]
        if start <= last_end:
            last_end = max(end, last_end)
        else:
            merged.append([start, end])

    return merged


if __name__ == "__main__":
    # Test cases
    print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
    # [[1,6],[8,10],[15,18]]

    print(merge_intervals([[1,4],[4,5]]))
    # [[1,5]]  ← touching intervals merge

    print(merge_intervals([[1,4],[2,3]]))
    # [[1,4]]  ← one fully inside another

    print(merge_intervals([[1,2]]))
    # [[1,2]]  ← single interval