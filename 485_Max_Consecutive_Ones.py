def findMaxConsecutiveOnes(nums):
    res = 0
    counts = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            counts += 1
        else:
            counts = 0
        res = max(res, counts)
    return res

if __name__ == '__main__':
    print(findMaxConsecutiveOnes(nums = [1,1,0,1,1,1]))
    print(findMaxConsecutiveOnes(nums = [1,0,1,1,0,1]))