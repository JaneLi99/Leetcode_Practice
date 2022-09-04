"""
Tangerine OA 3
Write a function that given tow integers N and K, return the minimum number of glasses that are needed to
contain exactly K liters of water into glasses. If it is not possible to pour exactly K liters of water into
glasses then the function should return -1.
Examples:
    1. Given N = 5 and K = 8, the function should return 2. There are five glasses of capacity 1, 2, 3, 4 and 5.
    You can use two glasses with capacity 3 and 5 to hold 8 luters of water.
    2. Given N = 4 and K = 10, the function should return 4. You must use all the glasses to contain 10 liters
    of water.
    3. Given N = 1 and K = 2, the function should return -1. There is only one glass with capacity 1, so you
    cannot pour liters of water.
    4. Given N = 10 and K = 5, the function should return 1. You can use the glass with capacity 5.
"""
def solution(N, K):
    glass_list = [i for i in range(N, 0, -1)]

    if K > sum(glass_list):
        return -1

    res = 0
    while K > 0:
        if K in glass_list:
            return 1

        for j in glass_list:
            if K >= j:
                K -= j
                res += 1
    return res

if __name__ == '__main__':
    print(solution(N = 5, K = 8))
    print(solution(N = 4, K = 10))
    print(solution(N = 1, K = 5))
    print(solution(N = 10, K = 5))
