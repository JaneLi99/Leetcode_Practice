def maxProduct(nums):
    ans = nums[0]
    maxprod, minprod = ans, ans
    for i in range(1, len(nums)):
        if nums[i] < 0:
            maxprod, minprod = minprod, maxprod
        maxprod = max(nums[i], maxprod * nums[i])
        minprod = min(nums[i], minprod * nums[i])
        ans = max(ans, maxprod)
    return ans

if __name__ == '__main__':
    print(maxProduct(nums = [2,3,4,-2,4]))
    print(maxProduct(nums = [-2,0,-1]))
    print(maxProduct(nums = [0,5,1,3,4]))
