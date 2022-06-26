def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # Solution with using two for loops
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    # Solution with using Map
    prevMap = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
        return

if __name__ == '__main__':
    print(twoSum([2,7,11,15], 9))
    print(twoSum([3,2,4], 6))
    print(twoSum([3,3], 6))

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Input: nums = [3,3], target = 6
# Output: [0,1]

