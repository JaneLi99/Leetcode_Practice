# One line Solution
from itertools import combinations

def combine(n, k):
    return list(combinations(range(1, n + 1), k))

# Another Solution
def combine_2(n, k):
    res = []
    backtrack(1, n, [], res, k)
    return res

def backtrack(index, n, curr, res, k):
    if (len(curr) == k):
        res.append(curr[:])
        return
    for i in range(index, n + 1):
        curr.append(i)
        backtrack(i + 1, n, curr, res, k)
        curr.pop()

if __name__ == '__main__':
    print(combine(n = 4, k = 2))
    print(combine(n = 1, k = 1))

    print(combine_2(n=4, k=2))
    print(combine_2(n=1, k=1))