def minOperations(nums1, nums2):
    sum_1, sum_2 = sum(nums1), sum(nums2)
    if sum_1 == sum_2:
        return 0

    if sum_1 < sum_2:
        nums_smaller, nums_greater = nums1, nums2
    else:
        nums_smaller, nums_greater = nums2, nums1

    all_ptr = sorted([num - 1 for num in nums_greater] + [6 - num for num in nums_smaller], reverse = True)

    res = 0
    tmp = 0
    diff = abs(sum_1 - sum_2)
    for ptr in all_ptr:
        tmp += ptr
        res += 1
        if diff <= tmp:
            return res
    return -1

if __name__ == '__main__':
    print(minOperations(nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]))
    print(minOperations(nums1 = [1,1,1,1,1,1,1], nums2 = [6]))
    print(minOperations(nums1 = [6,6], nums2 = [1]))