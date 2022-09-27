# Solution, but time limit exceeded
def minimumAbsDifference(arr):
    if len(arr) == 2:
        return [arr]

    min_abs_diff = float('inf')
    res = []
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            diff = abs(arr[i] - arr[j])
            diff_pair = [arr[i], arr[j]]
            diff_pair.sort()
            if diff < min_abs_diff:
                min_abs_diff = diff
                res = [diff_pair]
            elif diff == min_abs_diff:
                res.append(diff_pair)
    res.sort()
    return res

# Another solution, more efficient
def minimumAbsDifference_2(arr):
    arr.sort()
    mindiff = abs(arr[1] - arr[0])
    allpairs = []

    for i in range(len(arr) - 1):
        temp_min = abs(arr[i + 1] - arr[i])
        if temp_min < mindiff:
            mindiff = temp_min
            allpairs.clear()
            res = [arr[i], arr[i + 1]]
            allpairs.append(res)
        elif temp_min == mindiff:
            res = [arr[i], arr[i + 1]]
            allpairs.append(res)
    return allpairs

if __name__ == '__main__':
    print(minimumAbsDifference(arr = [4,2,1,3]))
    print(minimumAbsDifference(arr = [1,3,6,10,15]))
    print(minimumAbsDifference(arr = [3,8,-10,23,19,-4,-14,27]))