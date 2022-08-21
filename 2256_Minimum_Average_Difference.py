def minimumAverageDifference(nums):
    if len(nums) == 0:
        return 0

    res = []
    for i in range(len(nums)):
        part1 = sum(nums[:i + 1]) // (i + 1)
        if len(nums[i + 1:]) != 0:
            part2 = sum(nums[i + 1:]) // (len(nums) - i - 1)
        else:
            part2 = 0
        diff = abs(part1 - part2)
        res.append(diff)

    idx = res.index(min(res))
    return idx

# Another Solution (More efficient)
def minimumAverageDifference_2(nums):
    N = len(nums)
    left = 0
    right = sum(nums)
    minindex = 0
    minnum = 10 ** 20

    for i in range(N):
        left += nums[i]
        right -= nums[i]
        if i + 1 == N:
            r = abs(left // i + 1)
        else:
            r = abs(left // (i + 1) - right // (N - i - 1))

        if r < minnum:
            minnum = r
            minindex = i

    return minindex

if __name__ == '__main__':
    print(minimumAverageDifference(nums = [2,5,3,9,5,3]))
    print(minimumAverageDifference(nums = [0]))

    print(minimumAverageDifference_2(nums = [2,5,3,9,5,3]))
    print(minimumAverageDifference_2(nums = [0]))