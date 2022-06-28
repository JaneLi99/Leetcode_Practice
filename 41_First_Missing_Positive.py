# Complicated Solution
def firstMissingPositive(nums):
    nums.sort()
    new_nums = []
    for i in range(len(nums)):
        if nums[i] not in new_nums:
            new_nums.append(nums[i])

    while min(new_nums) <= 0:
        if min(new_nums) <= 0:
            new_nums.remove(min(new_nums))
        if len(new_nums) == 0:
            return 1

    if min(new_nums) > 1 or (len(new_nums) == 1 and new_nums[0] != 1):
        return 1
    if len(new_nums) == 1 and new_nums[0] == 1:
        return 2

    temp = 1
    for i in range(len(new_nums) - 1):
        if new_nums[i + 1] - new_nums[i] == 1:
            temp = temp + 1
            if temp == len(new_nums):
                return new_nums[i + 1] + 1
        else:
            return new_nums[i] + 1

# Simple Solution
def firstMissingPositive(nums):
    nums.append(0)
    N = len(nums)

    for i in range(N):
        if nums[i] < 0 or nums[i] > N:
            nums[i] = 0

    temp = nums[0]
    for i in range(N):
        if nums[i] > 0:
            nums[nums[i] % N - 1] += N
    if nums[0] == temp:
        return 1
    for i in range(N):
        if nums[i] // N == 0:
            return i + 1
    return N


if __name__ == '__main__':
    print(firstMissingPositive(nums = [0,2,2,1,1]))
    print(firstMissingPositive(nums = [1,2,0]))
    print(firstMissingPositive(nums = [3,4,-1,1]))
    print(firstMissingPositive(nums = [7,8,9,11,12]))