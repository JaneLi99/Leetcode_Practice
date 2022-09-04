def medianSlidingWindow(nums, k):
    res = []
    for i in range(len(nums) - k + 1):
        subnums = sorted(nums[i: i + k])
        if k % 2 == 1:
            median = subnums[k // 2]
        else:
            median = (subnums[(k // 2) - 1] + subnums[(k // 2)]) / 2
        res.append(float("{:.5f}".format(median)))
    return res

if __name__ == '__main__':
    print(medianSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
    print(medianSlidingWindow(nums = [1,2,3,4,2,3,1,4,2], k = 3))
