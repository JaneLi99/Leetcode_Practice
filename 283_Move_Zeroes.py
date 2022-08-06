def moveZeroes(nums):
    for num in nums:
        if num == 0:
            nums.remove(num)
            nums.append(0)
    return nums

if __name__ == '__main__':
    print(moveZeroes(nums = [0,1,0,3,12]))
    print(moveZeroes(nums= [0]))