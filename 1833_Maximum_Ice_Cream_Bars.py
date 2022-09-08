def maxIceCream(costs, coins):
    if sum(costs) <= coins:
        return len(costs)

    if min(costs) > coins:
        return 0

    costs.sort()
    counts = 0
    for i in range(len(costs)):
        if costs[i] <= coins:
            counts += 1
            coins -= costs[i]
    return counts

if __name__ == '__main__':
    print(maxIceCream(costs = [1,3,2,4,1], coins = 7))
    print(maxIceCream(costs = [10,6,8,7,7,8], coins = 5))
    print(maxIceCream(costs = [1,6,3,1,2,5], coins = 20))