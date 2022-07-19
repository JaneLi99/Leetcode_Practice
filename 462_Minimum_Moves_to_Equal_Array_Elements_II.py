def minMoves2(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    res = 0
    for i in range(len(nums)):
        res = res + abs(nums[i] - median)
    return res

if __name__ == '__main__':
    print(minMoves2(nums = [1,2,3]))
    print(minMoves2(nums = [1,10,2,9]))
    print(minMoves2(nums = [1,0,0,8,6]))