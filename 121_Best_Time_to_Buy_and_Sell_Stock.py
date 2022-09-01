# Time limit exceeded
def maxProfit(prices):
    res = []
    for i in range(len(prices) - 1):
        if prices[i] < max(prices[i + 1:]):
            res.append(max(prices[i + 1:]) - prices[i])

    if not res:
        return 0
    return max(res)

# Another Solution, more efficient
def maxProfit_2(prices):
    max_profit = max_price = 0
    n = len(prices)
    for i in range(n - 1, -1, -1):
        max_price = max(max_price, prices[i])
        max_profit = max(max_profit, max_price - prices[i])

    return max_profit

if __name__ == '__main__':
    print(maxProfit(prices = [7,1,5,3,6,4]))
    print(maxProfit(prices = [7,6,4,3,1]))

    print(maxProfit_2(prices=[7, 1, 5, 3, 6, 4]))
    print(maxProfit_2(prices=[7, 6, 4, 3, 1]))
