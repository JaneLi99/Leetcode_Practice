def singleNumber(nums):
    for elem in nums:
        if nums.count(elem) == 1:
            return elem


class Solution:
    def singleNumber(self, nums):
        return

if __name__ == '__main__':
    print(singleNumber(nums = [2,2,1]))
    print(singleNumber(nums = [1]))
    print(singleNumber(nums = [4,1,2,1,2]))

