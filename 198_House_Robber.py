def rob(nums):
    if len(nums) == 1:
        return nums[0]

    dp = {}
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
    return max(dp.values())

if __name__ == '__main__':
    print(rob(nums = [1,2,3,1]))
    print(rob(nums = [2,7,9,3,1]))