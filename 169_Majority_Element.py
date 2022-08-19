from collections import Counter

def majorityElement(nums):
    counter = Counter(nums)
    for k, v in counter.items():
        if v > len(nums) // 2:
            return k

if __name__ == '__main__':
    print(majorityElement(nums = [3,2,3]))
    print(majorityElement(nums = [2,2,1,1,1,2,2]))
    print(majorityElement(nums = [5,5,1,1,1]))