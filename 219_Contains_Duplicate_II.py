"""
Given an integer array nums and an integer k,
return true if there are two distinct indices i and j in the array
such that nums[i] == nums[j] and abs(i - j) <= k.
"""
def containsNearbyDuplicate(nums, k):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j] and abs(i - j) <= k:
                return True
    return False

# Another Solution, more efficient
def containsNearbyDuplicate_2(nums, k):
    idx_dict = {}
    for idx, ele in enumerate(nums):
        if idx_dict.get(ele) == None:
            idx_dict[ele] = idx
        else:
            if abs(idx_dict[ele] - idx) <= k:
                return True
            idx_dict[ele] = idx
    return False

if __name__ == '__main__':
    print(containsNearbyDuplicate(nums = [1,2,3,1], k = 3))
    print(containsNearbyDuplicate(nums = [1,0,1,1], k = 1))
    print(containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))

    print(containsNearbyDuplicate_2(nums=[1, 2, 3, 1], k=3))
    print(containsNearbyDuplicate_2(nums=[1, 0, 1, 1], k=1))
    print(containsNearbyDuplicate_2(nums=[1, 2, 3, 1, 2, 3], k=2))