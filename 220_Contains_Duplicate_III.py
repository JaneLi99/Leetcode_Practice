"""
Given an integer array nums and two integers k and t,
return true if there are two distinct indices i and j in the array
such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.
"""
def containsNearbyAlmostDuplicate(nums, k, t):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if abs(nums[i] - nums[j]) <= t and abs(i - j) <= k:
                return True
    return False

# Another Solution, more efficient
from sortedcontainers import SortedList

def containsNearbyAlmostDuplicate_2(nums, k, t):
    SList = SortedList()
    for i in range(len(nums)):
        if i > k:
            SList.remove(nums[i - k - 1])

        ind = SortedList.bisect_left(SList, nums[i])
        if ind < len(SList):
            if SList[ind] - nums[i] <= t:
                return True
        if ind > 0:
            if nums[i] - SList[ind - 1] <= t:
                return True

        SList.add(nums[i])

    return False

if __name__ == '__main__':
    print(containsNearbyAlmostDuplicate(nums = [1,2,3,1], k = 3, t = 0))
    print(containsNearbyAlmostDuplicate(nums = [1,0,1,1], k = 1, t = 2))
    print(containsNearbyAlmostDuplicate(nums = [1,5,9,1,5,9], k = 2, t = 3))

    print(containsNearbyAlmostDuplicate_2(nums=[1, 2, 3, 1], k=3, t=0))
    print(containsNearbyAlmostDuplicate_2(nums=[1, 0, 1, 1], k=1, t=2))
    print(containsNearbyAlmostDuplicate_2(nums=[1, 5, 9, 1, 5, 9], k=2, t=3))