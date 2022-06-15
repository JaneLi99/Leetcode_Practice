def threeSumClosest(nums, target):
    res = sum(nums[:3])
    nums.sort()

    for i in range(len(nums) - 2):
        l = i + 1
        r = len(nums) - 1
        while l < r:
            curr_sum = nums[i] + nums[l] + nums[r]
            if abs(curr_sum - target) < abs(res - target):
                res = curr_sum
            if curr_sum < target:
                l = l + 1
            else:
                r = r - 1

    return res

if __name__ == '__main__':
    threeSumClosest(nums = [-1,0,1,2,-1,-4], target = -7)
    threeSumClosest(nums = [3,-1,0,-2,1,-4], target = 5)
    threeSumClosest(nums = [0, 0, 0], target = 1)
    threeSumClosest(nums = [-1,2,1,-4], target = 1)