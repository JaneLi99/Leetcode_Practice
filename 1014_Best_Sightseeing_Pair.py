# Solution, but time limit exceeded
def maxScoreSightseeingPair(values):
    max_score = 0
    for i in range(len(values) - 1):
        for j in range(i + 1, len(values)):
            score = values[i] + values[j] + i - j
            max_score = max(max_score, score)
    return max_score

# Another Solution, more efficient
def maxScoreSightseeingPair_2(values):
    res = cur = 0
    for i, value in enumerate(values):
        res = max(value + cur - i, res)
        if value + i > cur:
            cur = value + i
    return res

if __name__ == '__main__':
    print(maxScoreSightseeingPair(values = [8,1,5,2,6]))
    print(maxScoreSightseeingPair(values = [1,2]))

    print(maxScoreSightseeingPair_2(values = [8,1,5,2,6]))
    print(maxScoreSightseeingPair_2(values = [1,2]))