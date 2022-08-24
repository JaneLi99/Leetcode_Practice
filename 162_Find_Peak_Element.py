def findPeakElement(nums):
    max_num = max(nums)
    index = nums.index(max_num)
    return index

if __name__ == '__main__':
    print(findPeakElement(nums = [1,2,3,1]))
    print(findPeakElement(nums = [1,2,1,3,5,6,4]))