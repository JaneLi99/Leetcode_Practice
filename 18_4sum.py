def fourSum(nums, target):
    nums.sort()
    if not nums or len(nums) < 4:
        return []

    result = []
    nums.sort()
    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j -1]:
                continue
            sumA = nums[i] + nums[j]
            left = j + 1
            right = len(nums) - 1
            while left <right:
                sumB = sumA + nums[left] + nums[right]
                if sumB == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif sumB < target:
                    left += 1
                else:
                    right -= 1
    # print(result)
    return result



if __name__ == '__main__':
    fourSum(nums = [1,0,-1,0,-2,2], target = 0)
    fourSum(nums = [2,2,2,2,2], target = 8)
    fourSum(nums = [-3,-1,0,2,4,5], target = 0)