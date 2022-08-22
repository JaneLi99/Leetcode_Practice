"""
Given an integer array nums,
return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""
def containsDuplicate(nums):
    nums_set = set(nums)
    if len(nums_set) < len(nums):
        return True
    return False

if __name__ == '__main__':
    print(containsDuplicate(nums = [1,2,3,1]))
    print(containsDuplicate(nums = [1,2,3,4]))
    print(containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2]))