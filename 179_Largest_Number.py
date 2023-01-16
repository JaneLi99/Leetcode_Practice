def largestNumber(nums):
    if not any(map(bool, nums)):
        return '0'

    nums = list(map(str, nums))
    if len(nums) < 2:
        return "".join(nums)

    def compare(x, y):
        return (int(nums[x] + nums[y])) > (int(nums[y] + nums[x]))

    for x in range(len(nums) - 1):
        y = x + 1
        while x < len(nums) and y < len(nums):
            if not compare(x, y):
                nums[x], nums[y] = nums[y], nums[x]
            y += 1

    return "".join(nums)

if __name__ == '__main__':
    print(largestNumber(nums = [10,2]))
    print(largestNumber(nums = [3,30,34,5,9]))