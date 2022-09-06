def rob(nums):
    num1, num2, num3, num4 = 0, 0, 0, 0
    tmp, tmp1 = 0, 0
    if len(nums) == 1: return nums[0]
    for i in range(0, len(nums) - 1):
        tmp = max(nums[i] + num2, num1)
        num2 = num1
        num1 = tmp
    for j in range(1, len(nums)):
        tmp1 = max(nums[j] + num4, num3)
        num4 = num3
        num3 = tmp1

    return max(tmp1, tmp)

if __name__ == '__main__':
    print(rob(nums = [2,3,2]))
    print(rob(nums = [1,2,3,1]))
    print(rob(nums = [1,2,3]))