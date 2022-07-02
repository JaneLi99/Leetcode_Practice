def threeSum(nums):
    # Solution with using two for loops
    # if len(nums) < 3:
    #     return []
    #
    # nums = sorted(nums)
    # result = []
    #
    # for i in range(len(nums) - 1):
    #     for j in range(i + 1, len(nums)):
    #         two_sum = nums[i] + nums[j]
    #         if -two_sum in nums[j + 1:]:
    #             m = nums[j + 1:].index(-two_sum)
    #             if [nums[i], nums[j], nums[j + 1:][m]] not in result:
    #                 result.append([nums[i], nums[j], nums[j + 1:][m]])
    # return result

    n = len(nums)
    result = []
    nums.sort()

    for i in range(n - 2):
        if nums[i] + nums[i + 1] + nums[i + 2] > 0:
            break
        if nums[i] + nums[n - 2] + nums[n - 1] < 0:
            continue
        if 0 < i and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, n - 1
        while l < r:
            tmp = nums[i] + nums[l] + nums[r]
            if tmp == 0:
                result.append([nums[i], nums[l], nums[r]])
                while l + 1 < r and nums[l] == nums[l + 1]:
                    l += 1
                l += 1
                while l < r - 1 and nums[r] == nums[r - 1]:
                    r -= 1
                r -= 1
            elif tmp < 0:
                l += 1
            else:
                r -= 1

    print(result)
    return result

if __name__ == '__main__':
    threeSum(nums = [-1,0,1,2,-1,-4])
    threeSum(nums=[3,-1,0,-2,1,-4])