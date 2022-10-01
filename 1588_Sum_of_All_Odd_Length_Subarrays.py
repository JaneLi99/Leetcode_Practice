def sumOddLengthSubarrays(arr):
    if len(arr) == 2:
        return sum(arr)

    i = 1
    sum_num = 0
    max_range = len(arr)
    while i <= max_range:
        for j in range(max_range - i + 1):
            sum_num += sum(arr[j: j + i])
            print(i, j, arr[j: j + i])
        i = i + 2
    return sum_num

if __name__ == '__main__':
    print(sumOddLengthSubarrays(arr = [1,4,2,5,3]))
    print(sumOddLengthSubarrays(arr = [1,2]))
    print(sumOddLengthSubarrays(arr = [7,6,8,6]))