def minMaxGame(nums):
    if len(nums) == 1:
        return nums[0]

    i = 0
    while i < len(nums) - 1:
        if (i // 2) % 2 == 0:
            min_num = min(nums[i], nums[i + 1])
            nums.append(min_num)
        else:
            max_num = max(nums[i], nums[i + 1])
            nums.append(max_num)
        i += 2

    return nums[-1]

if __name__ == '__main__':
    print(minMaxGame(nums = [1,3,5,2,4,8,2,2]))
    print(minMaxGame(nums = [3]))
