def missingNumber(nums):
    num_range = len(nums)
    non_miss_list = list(range(num_range + 1))

    for num in non_miss_list:
        if num not in nums:
            return num

if __name__ == '__main__':
    print(missingNumber(nums = [3,0,1]))
    print(missingNumber(nums = [0,1]))
    print(missingNumber(nums = [9,6,4,2,3,5,7,0,1]))