def search(nums, target):
    if target in nums:
        if len(nums) == 1 and nums[0] == target:
            return 0
        else:
            return nums.index(target)
    else:
        return -1


if __name__ == '__main__':
    print(search(nums = [4,5,6,7,0,1,2], target = 0))
    print(search(nums = [4,5,6,7,0,1,2], target = 3))
    print(search(nums = [1], target = 0))
    print(search(nums=[1, 3], target=1))