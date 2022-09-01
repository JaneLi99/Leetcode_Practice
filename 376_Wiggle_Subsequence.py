def wiggleMaxLength(nums):
    a, b, n = 1, 1, len(nums)
    for i in range(1, n):
        if nums[i - 1] < nums[i]:
            a = b + 1
        elif nums[i - 1] > nums[i]:
            b = a + 1
    return max(a, b)

if __name__ == '__main__':
    print(wiggleMaxLength(nums = [1,7,4,9,2,5]))
    print(wiggleMaxLength(nums = [1,17,5,10,13,15,10,5,16,8]))
    print(wiggleMaxLength(nums = [1,2,3,4,5,6,7,8,9]))