def combinationSum(candidates, target):
    candidates.sort()
    dp = [[] for _ in range(target + 1)]

    for c in candidates:
        for i in range(target + 1):
            if i < c:
                continue
            if i == c:
                dp[i].append([c])
            else:
                for blist in dp[i - c]:
                    dp[i].append(blist + [c])

    return dp[target]


if __name__ == '__main__':
    print(combinationSum(candidates = [2,3,6,7], target = 7))
    print(combinationSum(candidates = [2,3,5], target = 8))
    print(combinationSum(candidates = [2], target = 1))

