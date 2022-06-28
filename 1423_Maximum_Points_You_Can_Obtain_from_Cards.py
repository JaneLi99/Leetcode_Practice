def maxScore(cardPoints, k):
    if k == len(cardPoints):
        return sum(cardPoints)

    l = 0
    n = len(cardPoints) - k
    total = sum(cardPoints[n:])
    res = total

    while n < len(cardPoints):
        total = total + (cardPoints[l] - cardPoints[n])
        res = max(res, total)
        l = l + 1
        n = n + 1
    return res


if __name__ == '__main__':
    print(maxScore(cardPoints = [7,2,3,4,5,6,1], k = 3))
    print(maxScore(cardPoints = [2,2,2], k = 2))
    print(maxScore(cardPoints = [9,7,7,9,7,7,9], k = 7))
    print(maxScore(cardPoints = [100,40,17,9,73,75], k = 3))
