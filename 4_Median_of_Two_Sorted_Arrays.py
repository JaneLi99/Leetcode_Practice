def findMedianSortedArrays(nums1, nums2):
    combine_list = []
    for m in range(len(nums1)):
        combine_list.append(nums1[m])
    for n in range(len(nums2)):
        combine_list.append(nums2[n])
    combine_list = sorted(combine_list)
    reminder = len(combine_list) % 2
    index = int(len(combine_list) / 2)
    if reminder == 0:
        median = (combine_list[index - 1] + combine_list[index]) / 2
    else:
        median = combine_list[index]
    return median


if __name__ == '__main__':
    print(findMedianSortedArrays([1,2], [3,4]))
    print(findMedianSortedArrays([1,7], [2,5,6]))