def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k = k + 1
    return k

if __name__ == '__main__':
    print(removeElement(nums = [3,2,2,3], val = 3))
    print(removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))