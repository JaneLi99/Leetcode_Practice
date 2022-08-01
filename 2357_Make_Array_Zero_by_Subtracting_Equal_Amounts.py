def minimumOperations(nums):
    # Check if all the elements are 0
    counts = 0
    for i in range(len((nums))):
        if nums[i] == 0:
            counts += 1
    if counts == len(nums):
        return 0

    nums = set(nums)
    if 0 in nums:
        nums.remove(0)

    times = 0
    nums = list(nums)
    while max(nums) != 0:
        if 0 in nums:
            nums.remove(0)
        subtract = min(nums)
        new_nums = []
        for j in range(len(nums)):
            if nums[j] > 0:
                new_nums.append(nums[j] - subtract)
        nums = new_nums
        times = times + 1
    return times

if __name__ == '__main__':
    print(minimumOperations(nums = [1, 5, 0, 3, 5, 0]))
    print(minimumOperations(nums = [1, 1, 4, 6, 2, 9, 4]))
    print(minimumOperations(nums = [0]))
    print(minimumOperations(nums = [0, 0, 0, 0]))