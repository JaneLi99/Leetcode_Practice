from collections import defaultdict

def numFactoredBinaryTrees(arr):
    arr.sort()
    l = defaultdict(int)
    for a in arr:
        temp = 1
        for b in arr:
            if b > a:
                break
            temp += (l[b] * l[a / b])
        l[a] = temp

    return sum(l.values()) % (10 ** 9 + 7)

if __name__ == '__main__':
    print(numFactoredBinaryTrees(arr = [2,4]))
    print(numFactoredBinaryTrees(arr = [2,4,5,10]))
    print(numFactoredBinaryTrees(arr = [18,3,6,2]))