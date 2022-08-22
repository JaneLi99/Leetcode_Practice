from collections import Counter

def singleNumber(nums):
    dict = Counter(nums)
    for k, v in dict.items():
        if v == 1:
            return k

if __name__ == '__main__':
    print(singleNumber(nums = [2,2,3,2]))
    print(singleNumber(nums = [0,1,0,1,0,1,99]))
    print(singleNumber(nums = [0,1]))

