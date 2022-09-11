def minCostClimbingStairs(cost):
    dp = [0] * len(cost)
    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, len(cost)):
        dp[i] += cost[i] + min(dp[i - 2], dp[i - 1])
    return min(dp[-2], dp[-1])

if __name__ == '__main__':
    print(minCostClimbingStairs(cost = [10,15,20]))
    print(minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1]))