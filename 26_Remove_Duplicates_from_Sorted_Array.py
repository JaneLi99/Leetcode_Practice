def removeDuplicates(nums):
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums [i]
            k = k + 1
    return k

if __name__ == '__main__':
    print(removeDuplicates(nums = [1, 1, 2]))
    print(removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))
