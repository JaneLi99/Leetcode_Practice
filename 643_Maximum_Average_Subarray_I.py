# Solution, but time limit exceeded
def findMaxAverage(nums, k):
    print(nums[:k])
    max_avg = 0
    for i in range(len(nums) - k + 1):
        avg = sum(nums[i: i + k]) / k
        max_avg = max(max_avg, avg)
    return max_avg

# Solution, more efficient
def findMaxAverage_2(nums, k):
    max_avg = ans = sum(nums[:k])
    for i, n in enumerate(nums[k:]):
        ans += n - nums[i]
        max_avg = max(max_avg, ans)
    return max_avg * 1.0 / k

if __name__ == '__main__':
    print(findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4))
    print(findMaxAverage(nums = [5], k = 1))

    print(findMaxAverage_2(nums=[1, 12, -5, -6, 50, 3], k=4))
    print(findMaxAverage_2(nums=[5], k=1))