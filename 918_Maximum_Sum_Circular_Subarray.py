def maxSubarraySumCircular(nums):
    dp = [1 for _ in range(len(nums))]
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], nums[i] + dp[i - 1])

    dp1 = [1 for _ in range(len(nums))]
    dp1[0] = nums[0]
    for i in range(1, len(nums)):
        dp1[i] = min(dp1[i - 1] + nums[i], nums[i])

    res2 = sum(nums) - min(dp1)
    res1 = max(dp)

    if res2 != 0:
        return max(res2, res1)
    return res1

if __name__ == '__main__':
    print(maxSubarraySumCircular(nums = [1,-2,3,-2]))
    print(maxSubarraySumCircular(nums = [5,-3,5]))
    print(maxSubarraySumCircular(nums = [-3,-2,-3]))