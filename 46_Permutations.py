def permute(nums):
    if len(nums) <= 1:
        return [nums]

    res = []
    for i, num in enumerate(nums):
        n = nums[:i] + nums[i + 1:]
        for y in permute(n):
            res.append([num] + y)

    return res

if __name__ == '__main__':
    print(permute(nums = [1,2,3]))
    print(permute(nums = [0,1]))
    print(permute(nums = [1]))