from collections import Counter

def minWindow(s, t):
    if len(t) > len(s) or t == "":
        return ""

    idx = []
    for i in range(len(s)):
        if s[i] in t:
            idx.append(i)
            t = t.replace(s[i], "")
        if t == "":
            break

    return idx



class Solution:
    def minWindow(self, s, t):
        return

if __name__ == '__main__':
    print(minWindow(s = "ADOBECODEBANC", t = "ABC"))
    print(minWindow(s = "a", t = "a"))
    print(minWindow(s = "a", t = "aa"))

    s = "ADOBECODEBANC"
    t = "ABC"

    lookup = Counter(t)
    print(lookup)
    overall_list = []
    for subt in t:
        index_list = []
        for i, ltr in enumerate(s):
            if ltr == subt:
                index_list.append(i)
        overall_list.append(index_list)
    print(overall_list)

    diff = []
