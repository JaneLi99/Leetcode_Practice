def wordBreak(s, wordDict):
    s = s.replace(s[:4], "")
    print(s)
    return


class Solution:
    def wordBreak(self, s, wordDict):
        return

if __name__ == '__main__':
    print(wordBreak(s = "leetcode", wordDict = ["leet","code"]))
    print(wordBreak(s = "applepenapple", wordDict = ["apple","pen"]))
    print(wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]))