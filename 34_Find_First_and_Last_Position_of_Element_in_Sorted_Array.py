def searchRange(nums, target):
    if target not in nums:
        return [-1, -1]

    res = []
    for i in range(len(nums)):
        if target == nums[i]:
            res.append(i)

    return [min(res),max(res)]



if __name__ == '__main__':
    print(searchRange(nums = [5,7,7,8,8,10], target = 8))
    print(searchRange(nums = [5,7,7,8,8,10], target = 6))
    print(searchRange(nums = [], target = 0))