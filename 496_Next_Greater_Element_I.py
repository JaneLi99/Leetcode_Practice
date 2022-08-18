def nextGreaterElement(nums1, nums2):
    res = []
    for i in range(len(nums1)):
        index = nums2.index(nums1[i])
        if index == len(nums2) - 1 or max(nums2[index + 1:]) <= nums1[i]:
            res.append(-1)
        else:
            for j in nums2[index + 1:]:
                if j > nums1[i]:
                    res.append(j)
                    break
    return res

if __name__ == '__main__':
    print(nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))
    print(nextGreaterElement(nums1 = [2,4], nums2 = [1,2,3,4]))
    print(nextGreaterElement(nums1 = [1,3,5,2,4], nums2 = [6,5,4,3,2,1,7]))