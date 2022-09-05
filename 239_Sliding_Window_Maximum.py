# Solution, time limit exceeded
def maxSlidingWindow(nums, k):
    res = []
    for i in range(len(nums) - k + 1):
        max_num = max(nums[i: i + k])
        res.append(max_num)
    return res

# Another Solution, more efficient
from collections import deque

def maxSlidingWindow_2(nums, k):
    q = deque()
    res = []
    for i, cur in enumerate(nums):
        while q and nums[q[-1]] <= cur:
            q.pop()
        q.append(i)
        if q[0] == i - k:
            q.popleft()
        if i >= k - 1:
            res.append(nums[q[0]])
    return res

if __name__ == '__main__':
    print(maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
    print(maxSlidingWindow(nums = [1], k = 1))

    print(maxSlidingWindow_2(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
    print(maxSlidingWindow_2(nums=[1], k=1))