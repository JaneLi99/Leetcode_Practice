def thirdMax(nums):
    nums = list(set(nums))
    if len(nums) < 3:
        return max(nums)
    nums.sort(reverse=True)
    return nums[2]

if __name__ == '__main__':
    print(thirdMax(nums = [3,2,1]))
    print(thirdMax(nums = [1,2]))
    print(thirdMax(nums = [2,2,3,1]))