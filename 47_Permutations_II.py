def permuteUnique(nums):
    res = []
    perm = []
    count = {n: 0 for n in nums}
    for n in nums:
        count[n] += 1

    def dfs():
        if len(perm) == len(nums):
            res.append(perm.copy())
            return
        for n in count:
            if count[n] > 0:
                perm.append(n)
                count[n] -= 1

                dfs()
                count[n] += 1
                perm.pop()

    dfs()
    return res

if __name__ == '__main__':
    print(permuteUnique(nums = [1,2,3]))
    print(permuteUnique(nums = [1,1,2]))
    print(permuteUnique(nums = [1]))