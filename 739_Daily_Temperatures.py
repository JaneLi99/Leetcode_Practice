def dailyTemperatures(temperatures):
    res = []
    for i in range(len(temperatures) - 1):
        for j in range(i, len(temperatures)):
            if temperatures[i] >= max(temperatures[j:]):
                res.append(0)
                break
            elif temperatures[i] < temperatures[j]:
                res.append(j - i)
                break
    res.append(0)
    return res

# Another Solution, more efficient
def dailyTemperatures_2(temperatures):
    res = [0] * len(temperatures)
    stack = [] # pair: [temp, index]

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            res[stackInd] = (i - stackInd)
        stack.append([t, i])
    return res

if __name__ == '__main__':
    print(dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73]))
    # Output: [1,1,4,2,1,1,0,0]
    print(dailyTemperatures(temperatures = [30,40,50,60]))
    # Output: [1,1,1,0]
    print(dailyTemperatures(temperatures = [55,38,53,81,61,93,97,32,43,78]))
    # Output: [3,1,1,2,1,1,0,1,1,0]
    print(dailyTemperatures(temperatures = [34,80,80,34,34,80,80,80,80,34]))
    # Output: [1,0,0,2,1,0,0,0,0,0]

    print(dailyTemperatures_2(temperatures = [73,74,75,71,69,72,76,73]))
    print(dailyTemperatures_2(temperatures = [30,40,50,60]))
    print(dailyTemperatures_2(temperatures = [55,38,53,81,61,93,97,32,43,78]))
    print(dailyTemperatures_2(temperatures = [34,80,80,34,34,80,80,80,80,34]))