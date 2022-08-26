def wordBreak(s, wordDict):
    dp = [False for _ in range(len(s) + 1)]
    dp[len(s)] = True

    for i in range(len(s) - 1, -1, -1):
        for word in wordDict:
            if (i + len(word)) <= len(s) and s[i:i + len(word)] == word:
                dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
    return dp[0]

if __name__ == '__main__':
    print(wordBreak(s = "leetcode", wordDict = ["leet","code"]))
    print(wordBreak(s = "applepenapple", wordDict = ["apple","pen"]))
    print(wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]))