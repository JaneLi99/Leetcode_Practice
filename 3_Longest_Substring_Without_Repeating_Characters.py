def lengthOfLongestSubstring(s):
    start = 0
    length = 0
    substring = {}

    for i in range(len(s)):
        if s[i] in substring and substring[s[i]] >= start:
            start = substring[s[i]] + 1
        length = max(length, i - start + 1)
        substring[s[i]] = i

    return length

if __name__ == '__main__':
    print(lengthOfLongestSubstring("abcabcbb"))
    print(lengthOfLongestSubstring("bbbb"))
    print(lengthOfLongestSubstring("pwwkew"))