from collections import Counter

def findDuplicate(nums):
    counts = Counter(nums)
    for key, val in counts.items():
        if val > 1:
            return key

if __name__ == '__main__':
    print(findDuplicate(nums = [1,3,4,2,2]))
    print(findDuplicate(nums = [3,1,3,4,2]))