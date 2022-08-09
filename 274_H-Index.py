def hIndex(citations):
    citations.sort()
    for i, v in enumerate(citations):
        if len(citations) - i <= v:
            return len(citations) - i
    return 0

# Another Solution
def hIndex_2(citations):
    N = len(citations)
    citations.sort()
    tmp = [0 for _ in range(N + 1)]
    for i, v in enumerate(citations):
        if v > N:
            tmp[N] += 1
        else:
            tmp[v] += 1
    total = 0
    for i in range(N, -1, -1):
        total += tmp[i]
        if total >= i:
            return i

if __name__ == '__main__':
    print(hIndex(citations = [3,0,6,1,5]))
    print(hIndex(citations = [1,3,1]))
    print(hIndex(citations = [0]))
    print(hIndex(citations = [100]))

    print(hIndex_2(citations=[3, 0, 6, 1, 5]))
    print(hIndex_2(citations=[1, 3, 1]))
    print(hIndex_2(citations=[0]))
    print(hIndex_2(citations=[100]))