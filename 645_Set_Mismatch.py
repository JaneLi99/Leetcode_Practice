from collections import Counter

def findErrorNums(nums):
    c = Counter(nums)
    l = [0, 0]
    for i in range(1, len(nums) + 1):
        if c[i] == 2:
            l[0] = i
        if c[i] == 0:
            l[1] = i
    return l

if __name__ == '__main__':
    print(findErrorNums(nums = [1, 2, 2, 4]))
    print(findErrorNums(nums = [1, 1]))
    print(findErrorNums(nums = [2, 2]))
    print(findErrorNums(nums = [3, 2, 3, 4, 6, 5]))