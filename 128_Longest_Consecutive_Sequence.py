def longestConsecutive(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1

    new_nums = set(nums)
    new_nums = list(new_nums)
    new_nums.sort()

    list_len = []
    length = 1
    for i in range(len(new_nums) - 1):
        if new_nums[i + 1] - new_nums[i] == 1:
            length = length + 1
            res = max(1, length)
            list_len.append(res)
        else:
            res = max(1, length)
            list_len.append(res)
            length = 1

    if len(list_len) == 0:
        return 1

    return max(list_len)

if __name__ == '__main__':
    print(longestConsecutive(nums = [100,4,200,1,3,2]))
    print(longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))
    print(longestConsecutive(nums = [1,2,0,1]))
    print(longestConsecutive(nums = [0, 0]))
    print(longestConsecutive(nums = [0, 0, 1, 2, 3, 5, 7, 8]))