def nextGreaterElements(nums):
    res = [0] * len(nums)
    s = []
    for i in range(2 * len(nums) - 1, -1, -1):
        while len(s) != 0 and s[-1] <= nums[i % len(nums)]:
            s.pop(-1)
        if len(s) == 0:
            res[i % len(nums)] = -1
        else:
            res[i % len(nums)] = s[-1]
        s.append(nums[i % len(nums)])
    return res


if __name__ == '__main__':
    print(nextGreaterElements(nums = [1,2,1]))
    print(nextGreaterElements(nums = [1,2,3,4,3]))