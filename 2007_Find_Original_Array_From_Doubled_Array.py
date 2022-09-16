# Time limit exceeded
def findOriginalArray(changed):
    changed.sort()
    i = 0
    res = []
    while len(changed) > i:
        org = changed[i]
        chd = changed[i] * 2
        if chd in changed[i + 1:]:
            res.append(org)
            changed.remove(org)
            changed.remove(chd)
        else:
            i += 1

    if len(changed) == 0:
        return res
    return []

# Another Solution, more efficient
from collections import Counter

def findOriginalArray_2(changed):
    n = len(changed)
    freq = Counter(changed)
    changed.sort()

    if n % 2 != 0:
        return []

    ans = []
    for i, v in enumerate(changed):
        if freq[v] > 0:
            if v == 0 and freq[0] < 2:
                return []
            if v * 2 not in freq or freq[v * 2] == 0:
                return []

            freq[v] -= 1
            freq[v * 2] -= 1
            ans.append(v)

    return ans

if __name__ == '__main__':
    print(findOriginalArray(changed = [1,3,4,2,6,8]))
    print(findOriginalArray(changed = [6,3,0,1]))
    print(findOriginalArray(changed = [1]))

    print(findOriginalArray_2(changed=[1, 3, 4, 2, 6, 8]))
    print(findOriginalArray_2(changed=[6, 3, 0, 1]))
    print(findOriginalArray_2(changed=[1]))