# Solution 1, O(n ^ 2)
from collections import Counter

def minWindow(s, t):
    lookup = Counter(t)
    mx = float("inf")
    output = ""
    S = len(s)

    def helper(a):
        for k, v in lookup.items():
            if k not in a or a[k] < v:
                return False
        return True

    for end in range(S):
        for start in range(end):
            tmp = Counter(s[start : end + 1])
            if helper(tmp):
                if end - start < mx:
                    mx = end - start
                    output = s[start : end + 1]
    return output

# Another Solution, more efficient
def minWindow_2(s, t):
    lookup = Counter(t)
    mx = float("inf")
    output = ""
    S = len(s)
    start, end = 0, 0
    count = len(lookup)

    while end < S:
        # End Pointer
        while end < S and count != 0:
            if s[end] in lookup:
                lookup[s[end]] -= 1
                if lookup[s[end]] == 0:
                    count -= 1
            end += 1

        # Start Pointer
        while start <= end and count == 0:
            if end - start < mx:
                mx = end - start
                output = s[start : end]
            if s[start] in lookup:
                lookup[s[start]] += 1
                if lookup[s[start]] > 0:
                    count += 1
            start += 1
    return output

if __name__ == '__main__':
    print(minWindow(s = "ADOBECODEBANC", t = "ABC"))
    print(minWindow(s = "a", t = "a"))
    print(minWindow(s = "a", t = "aa"))

    print(minWindow_2(s = "ADOBECODEBANC", t = "ABC"))
    print(minWindow_2(s="a", t="a"))
    print(minWindow_2(s="a", t="aa"))