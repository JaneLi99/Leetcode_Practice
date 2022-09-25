def getKth(lo, hi, k):
    nums = [i for i in range(lo, hi + 1)]

    power_list = []
    for i in range(lo, hi + 1):
        power = 0
        while i != 1:
            if i % 2 == 0:
                i = i / 2
            else:
                i = 3 * i + 1
            power += 1
        power_list.append(power)

    pair = []
    for i in range(len(nums)):
        pair.append([power_list[i], nums[i]])
    pair.sort()

    return pair[k - 1][1]

if __name__ == '__main__':
    print(getKth(lo = 12, hi = 15, k = 2))
    print(getKth(lo = 7, hi = 11, k = 4))