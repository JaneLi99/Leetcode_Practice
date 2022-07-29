def findAndReplacePattern(words, pattern):
    def get_pattern(s):
        lookup = {}
        output = []
        i = 0
        for c in s:
            if c in lookup:
                output.append(lookup[c])
            else:
                i = i + 1
                lookup[c] = i
                output.append(i)
        return output

    p = get_pattern(pattern)
    output = []
    for word in words:
        if get_pattern(word) == p:
            output.append(word)
    return output

# Another Solution
def findAndReplacePattern2(words, pattern):
    def check(s, p):
        m1, m2 = {}, {}
        for a, b in zip(s, p):
            if a not in m1:
                m1[a] = b
            if b not in m2:
                m2[b] = a

            if a != m2[b] or b != m1[a]:
                return False
        return True

    output = []
    for word in words:
        if check(word, pattern):
            output.append(word)
    return output

if __name__ == '__main__':
    print(findAndReplacePattern(words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"))
    print(findAndReplacePattern(words = ["a","b","c"], pattern = "a"))

    print(findAndReplacePattern2(words=["abc", "deq", "mee", "aqq", "dkd", "ccc"], pattern="abb"))
    print(findAndReplacePattern2(words=["a", "b", "c"], pattern="a"))