def maxSubArray(nums):
    maxsum = nums[0]
    currsum = 0

    for n in nums:
        if currsum < 0:
            currsum = 0
        currsum += n
        maxsum = max(currsum, maxsum)

    return maxsum


if __name__ == '__main__':
    maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    maxSubArray([1])
    maxSubArray([5,4,-1,7,8])
    maxSubArray([-2,-1,-1])