def getMaxLen(nums):
    pos = neg = res = 0
    for num in nums:
        if num > 0:
            pos += 1
            if neg != 0:
                neg += 1
            else:
                neg = 0

        elif num < 0:
            if neg > 0:
                pos, neg = neg + 1, 0
            else:
                pos, neg = 0, pos + 1

        else:
            pos = neg = 0

        res = max(res, pos)
    return res

if __name__ == '__main__':
    print(getMaxLen(nums = [1,-2,-3,4]))
    print(getMaxLen(nums = [0,1,-2,-3,-4]))
    print(getMaxLen(nums = [-1,-2,-3,0,1]))