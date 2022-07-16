def minMoves(nums):
    return sum(nums) - min(nums) * len(nums)

if __name__ == '__main__':
    print(minMoves(nums = [1,2,3]))
    print(minMoves(nums = [1,1,1]))