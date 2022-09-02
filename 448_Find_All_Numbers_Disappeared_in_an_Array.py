# Solution, but time limit exceeded
def findDisappearedNumbers(nums):
    n = len(nums)
    nums = list(set(nums))
    nums.sort()
    res = []
    for i in range(1, n + 1):
        if i not in nums:
            res.append(i)
    return res

# Another Solution, more efficient
def findDisappearedNumbers_2(nums):
    arr = set([i for i in range(1, len(nums) + 1)])
    return arr - set(nums)

if __name__ == '__main__':
    print(findDisappearedNumbers(nums = [4,3,2,7,8,2,3,1]))
    print(findDisappearedNumbers(nums = [1,1]))

    print(findDisappearedNumbers_2(nums=[4, 3, 2, 7, 8, 2, 3, 1]))
    print(findDisappearedNumbers_2(nums=[1, 1]))
