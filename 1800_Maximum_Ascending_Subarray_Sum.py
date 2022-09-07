def maxAscendingSum(nums):
    max_num = nums[0]
    sub_list = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            sub_list.append(nums[i])
        else:
            sub_list = [nums[i]]
        max_num = max(max_num, sum(sub_list))
    return max_num

if __name__ == '__main__':
    print(maxAscendingSum(nums = [10,20,30,5,10,50]))
    print(maxAscendingSum(nums = [10,20,30,40,50]))
    print(maxAscendingSum(nums = [12,17,15,13,10,11,12]))