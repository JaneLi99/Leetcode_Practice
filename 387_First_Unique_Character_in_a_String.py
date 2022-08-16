def firstUniqChar(s):
    for i in range(len(s)):
        if s[i] not in s[:i] and s[i] not in s[i + 1:]:
            return i
    return -1

if __name__ == '__main__':
    print(firstUniqChar(s = "leetcode"))
    print(firstUniqChar(s = "loveleetcode"))
    print(firstUniqChar(s = "aabb"))