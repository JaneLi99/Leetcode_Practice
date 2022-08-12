def lengthOfLIS(nums):
    N = len(nums)
    dp = [1] * N
    for n in range(N):
        for i in range(n):
            if nums[i] < nums[n]:
                dp[n] = max(dp[n], dp[i] + 1)

    return max(dp)
    # O(n ^ 2)

# Another Solution
from bisect import bisect_left

def lengthOfLIS_2(nums):
    tmp = [nums[0]]
    for n in nums:
        x = bisect_left(tmp, n)
        if x == len(tmp):
            tmp.append(n)
        elif tmp[x] > n:
            tmp[x] = n
    return len(tmp)
    # O(n * log n)

if __name__ == '__main__':
    print(lengthOfLIS(nums = [10,9,2,5,3,7,101,18]))
    # Output: 4
    # Explanation: The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
    print(lengthOfLIS(nums = [0,1,0,3,2,3]))
    # Output: 4
    print(lengthOfLIS(nums = [7,7,7,7,7,7,7]))
    # Output: 1

    print(lengthOfLIS_2(nums=[10, 9, 2, 5, 3, 7, 101, 18]))
    print(lengthOfLIS_2(nums=[0, 1, 0, 3, 2, 3]))
    print(lengthOfLIS_2(nums=[7, 7, 7, 7, 7, 7, 7]))