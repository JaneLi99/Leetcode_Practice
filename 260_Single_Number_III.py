from collections import Counter

def singleNumber(nums):
    dict = Counter(nums)
    res = []
    for k, v in dict.items():
        if v == 1:
            res.append(k)
    return res

if __name__ == '__main__':
    print(singleNumber(nums = [1,2,1,3,2,5]))
    print(singleNumber(nums = [-1,0]))
    print(singleNumber(nums = [0,1]))