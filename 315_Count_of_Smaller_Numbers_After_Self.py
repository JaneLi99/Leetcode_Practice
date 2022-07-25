from sortedcontainers import SortedList

def countSmaller(nums):
    # res = []
    # for i in range(len(nums)):
    #     j = 0
    #     counts = 0
    #     while j < len(nums[i + 1:]):
    #         if nums[i] > nums[i + 1:][j]:
    #             counts += 1
    #         j = j + 1
    #     res.append(counts)
    # return res

    s = SortedList()
    output = []
    for n in nums[::-1]:
        ans = SortedList.bisect_left(s, n)
        output.append(ans)
        s.add(n)
    return reversed(output)

if __name__ == '__main__':
    print(countSmaller(nums = [5,2,6,1]))
    print(countSmaller(nums = [-1]))
    print(countSmaller(nums = [-1, -1]))