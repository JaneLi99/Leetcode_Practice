def combinationSum4(nums, target):
    nums.sort()
    if nums[0] > target:
        return 0

    dp = [0] * (target + 1)
    dp[0] = 1

    for t in range(1, target + 1):
        for n in nums:
            if n <= t:
                dp[t] += dp[t - n]
    return dp[target]

if __name__ == '__main__':
    print(combinationSum4(nums = [1,2,3], target = 4))
    print(combinationSum4(nums = [9], target = 3))