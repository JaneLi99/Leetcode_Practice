def findMin(nums):
    res = []
    for i in range(len(nums) - 1):
        if nums[i] <= nums[i + 1]:
            continue
        else:
            res.extend(nums[i + 1:len(nums)])
            res.extend(nums[0:i + 1])
            return res[0]
    return nums[0]


if __name__ == '__main__':
    print(findMin([3, 4, 5, 1, 2]))
    print(findMin([4, 5, 6, 7, 0, 1, 2]))
    print(findMin([11, 13, 15, 17]))

