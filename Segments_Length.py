def segmentsLength(n, segments):
    segments.sort()
    max_length = abs(segments[0][1] - segments[0][0])
    # print(segments, max_length)
    for i in range(n - 1):
        if segments[i][1] > segments[i + 1][0]:
            tmp = abs(segments[i + 1][1] - segments[i + 1][0])
            max_length = max(max_length, tmp)
        else:
            max_length += abs(segments[i + 1][1] - segments[i + 1][0])
    return max_length

if __name__ == '__main__':
    print(segmentsLength(3, [[1,3], [5,7], [2,6]]))
    print(segmentsLength(2, [[2,3], [1,2]]))
    print(segmentsLength(5, [[1, 5], [4, 5], [2, 5], [0, 2], [10, 12]]))

