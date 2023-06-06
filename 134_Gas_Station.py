def canCompleteCircuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1

    gas_value = 0
    res = 0
    for i in range(len(gas)):
        gas_value = gas_value + gas[i] - cost[i]
        if gas_value < 0:
            gas_value = 0
            res = i + 1

    return res

if __name__ == '__main__':
    print(canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))
    print(canCompleteCircuit(gas = [2,3,4], cost = [3,4,3]))
