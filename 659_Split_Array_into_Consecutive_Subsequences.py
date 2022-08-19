from collections import Counter, defaultdict

def isPossible(nums):
    counter = Counter(nums)
    end = defaultdict(int)

    for num in nums:
        if counter[num]:
            counter[num] -= 1

            if end[num - 1]:
                end[num] += 1
                end[num - 1] -= 1
            elif counter[num + 1] and counter[num + 2]:
                counter[num + 1] -= 1
                counter[num + 2] -= 1
                end[num + 2] += 1
            else:
                return False
    return True

if __name__ == '__main__':
    print(isPossible(nums = [1,2,3,3,4,5]))
    print(isPossible(nums = [1,2,3,3,4,4,5,5]))
    print(isPossible(nums = [1,2,3,4,4,5]))