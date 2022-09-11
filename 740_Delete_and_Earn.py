def deleteAndEarn(nums):
    dp = [0] * (max(nums) + 1)
    for num in nums:
        dp[num] += num
    for i in range(1, len(dp) - 1):
        dp[i + 1] = max(dp[i], dp[i - 1] + dp[i + 1])
    return dp[-1]

if __name__ == '__main__':
    print(deleteAndEarn(nums = [3,4,2]))
    print(deleteAndEarn(nums = [2,2,3,3,3,4]))
    print(deleteAndEarn(nums = [2,5,5,5]))