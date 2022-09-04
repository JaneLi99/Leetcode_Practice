def intersect(nums1, nums2):
    res = []
    i = 0
    while i < len(nums1):
        if nums1[i] in nums2:
            res.append(nums1[i])
            nums2.remove(nums1[i])
            nums1.remove(nums1[i])
        else:
            i += 1
    return res

if __name__ == '__main__':
    print(intersect(nums1 = [1,2,2,1], nums2 = [2,2]))
    print(intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))