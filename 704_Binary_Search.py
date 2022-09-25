def search(nums, target):
    if target not in nums:
        return -1
    return nums.index(target)

if __name__ == '__main__':
    print(search(nums = [-1,0,3,5,9,12], target = 9))
    print(search(nums = [-1,0,3,5,9,12], target = 2))