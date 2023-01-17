def numJewelsInStones(jewels, stones):
    res = 0
    for i in stones:
        if i in jewels:
            res += 1
    return res

if __name__ == '__main__':
    print(numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))
    print(numJewelsInStones(jewels = "z", stones = "ZZ"))