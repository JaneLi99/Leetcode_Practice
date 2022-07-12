def subsets(nums):
    res = [[]]
    for i in nums:
        for lst in res:
            res = res + [lst + [i]]
    return res

if __name__ == '__main__':
    print(subsets(nums = [1, 2, 3]))
    print(subsets(nums = [0]))
    print(subsets(nums = [0, 1, 2, 3, 4]))
