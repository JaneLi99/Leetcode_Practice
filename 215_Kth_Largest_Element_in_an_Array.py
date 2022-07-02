def findKthLargest(nums, k):
    nums.sort()
    return nums[len(nums) - k]

if __name__ == '__main__':
    print(findKthLargest(nums = [3,2,1,5,6,4], k = 2))
    print(findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))