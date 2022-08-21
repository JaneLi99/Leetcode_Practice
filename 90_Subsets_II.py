import itertools

def subsetsWithDup(nums):
    if len(nums) == 1:
        return [[], nums]

    res = []
    for i in range(len(nums) + 1):
        for j in itertools.combinations(nums, i):
            subset = sorted(list(j))
            if subset not in res:
                res.append(subset)
    return res

if __name__ == '__main__':
    print(subsetsWithDup(nums = [1,2,2]))
    print(subsetsWithDup(nums = [0]))
    print(subsetsWithDup(nums = [4,4,4,1,4]))