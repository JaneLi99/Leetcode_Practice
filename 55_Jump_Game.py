def canJump(nums):
    n = len(nums)
    l = 0
    r = nums[0]

    while l < n:
        x = nums[l]

        if l > r:
            return False

        r = max(r, l + x)
        l += 1

    return True

if __name__ == '__main__':
    print(canJump(nums = [2,3,1,1,4]))
    print(canJump(nums = [3,2,1,0,4]))