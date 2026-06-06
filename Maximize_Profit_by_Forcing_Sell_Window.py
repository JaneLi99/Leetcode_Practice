# You are given two integer arrays:
# prices, where prices[i] is the stock price on day i
# plan, where:
# plan[i] = 0 means the bot plans to buy on day i
# plan[i] = 1 means the bot plans to sell on day i
# You are also given an integer k.
# You may choose exactly one contiguous subarray of length k and force every action in that subarray to become 1 (sell).
# Your task is to return the maximum total profit that can be achieved after applying this modification once.
# Profit Calculation
# If plan[i] = 1, then the bot earns prices[i]
# If plan[i] = 0, then the bot earns 0
# In other words, the total profit is the sum of prices[i] for all days where the action is sell.
# After selecting one window of length k, all 0s in that window become 1s, which may increase the total profit.
# Return the maximum possible total profit.
#
# Example 1
# Input: prices = [1, 3, 2, 5, 4], plan = [1, 0, 0, 1, 0], k = 2
# Output: 9
# Explanation:
# Original profit:
# Day 0: sell → +1
# Day 3: sell → +5
# So the original profit is 1 + 5 = 6.
# Now choose a window of length 2:
# Window [1, 2]: change plan from [0, 0] to [1, 1]
# Extra profit gained = 3 + 2 = 5
# New total profit = 6 + 5 = 11
# So the maximum profit is 11.
#
# Example 2
# Input: prices = [4, 2, 8], plan = [1, 1, 1], k = 2
# Output: 14
# Explanation:
# All days are already sells, so forcing any window to sell does not change anything.
# Total profit = 4 + 2 + 8 = 14.
#
# Example 3
# Input: prices = [5, 1, 3, 7], plan = [0, 0, 0, 0], k = 2
# Output: 10
# Explanation:
# Since all actions are buys, the original profit is 0.
# Choose the window [2, 3], and change it to sells:
# Extra profit = 3 + 7 = 10
# Maximum total profit = 10.

from typing import List


def maximizeProfit(prices: List[int], plan: List[int], k: int) -> int:
    n = len(prices)
    original_profit = 0
    for i in range(n):
        if plan[i] == 1:
            original_profit += prices[i]

    gain = [0] * n
    for i in range(n):
        if plan[i] == 0:
            gain[i] = prices[i]

    window_sum = sum(gain[:k])
    max_extra_profit = window_sum

    for right in range(k, n):
        window_sum += gain[right]
        window_sum -= gain[right - k]
        max_extra_profit = max(max_extra_profit, window_sum)

    return original_profit + max_extra_profit


def main():
    # Test case 1
    prices = [1, 3, 2, 5, 4]
    plan = [1, 0, 0, 1, 0]
    k = 2

    result = maximizeProfit(prices, plan, k)
    print("Test Case 1")
    print("Prices:", prices)
    print("Plan:", plan)
    print("k:", k)
    print("Result:", result)
    print()

    # Test case 2
    prices = [4, 2, 8]
    plan = [1, 1, 1]
    k = 2

    result = maximizeProfit(prices, plan, k)
    print("Test Case 2")
    print("Prices:", prices)
    print("Plan:", plan)
    print("k:", k)
    print("Result:", result)
    print()

    # Test case 3
    prices = [5, 1, 3, 7]
    plan = [0, 0, 0, 0]
    k = 2

    result = maximizeProfit(prices, plan, k)
    print("Test Case 3")
    print("Prices:", prices)
    print("Plan:", plan)
    print("k:", k)
    print("Result:", result)


if __name__ == "__main__":
    main()