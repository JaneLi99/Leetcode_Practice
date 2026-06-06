# Problem: Count Numbers That Are Powers of k
# Given an integer array nums and an integer k, return the number of elements in nums that are a power of k.
# An integer x is considered a power of k if there exists a non-negative integer n such that:
# 𝑥 = 𝑘 ^^ n
#
# Example 1
# Input: nums = [1,3,5,8,16], k = 2
# Output: 3
# Explanation: The numbers 1 (2^0), 8 (2^3), and 16 (2^4) are powers of 2.
# Function Signature
# int countPowers(int[] nums, int k)
#
# Constraints
# 1 ≤ nums.length ≤ 10^5
# 1 ≤ nums[i] ≤ 10^9
# 2 ≤ k ≤ 10^9
#
# Follow-up
# Can you solve this in O(n log_k(max(nums))) time without using extra space?

import math

def countPowers(nums, k):
    result = 0
    for i in nums:
        if math.log(i, k).is_integer():
            result += 1
    return result


def main():
    nums = [1, 3, 5, 8, 16]
    k = 2

    result = countPowers(nums, k)
    print("Input:", nums)
    print("k =", k)
    print("Output:", result)


if __name__ == "__main__":
    main()