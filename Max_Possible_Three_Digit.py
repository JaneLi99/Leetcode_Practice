"""
Write a function that given a three-digit integer N and an integer K, returns that maximum possible three-digit value
that can be obtained by perforing at most K increases by 1 of any digit in N.
Example:
    1. Given N = 512 and K = 10, the function should return 972. The result can be obtained by increasing the first
    digit of N four times and the second digit six times.
    2. Given N = 191 and K = 4, the function should return 591. The result can be obtained by increaseing the first
    digit of N four times.
    3. Given N = 285 and K = 20, the function should return 999. The result can be obtained by increasing the first
    digit of N seven times, the second digit once and the third digit four times.
"""
def solution(N, K):
    N = str(N)
    i = 0
    while K > 0 and i < len(N):
        tmp = 9 - int(N[i])
        if int(N[i]) < 9 and tmp <= K:
            N = N.replace(N[i], "9", 1)
        elif int(N[i]) < 9 and tmp > K:
            new_numer = str(int(N[i]) + K)
            N = N.replace(N[i], new_numer, 1)
        K -= tmp
        i += 1
    return int(N)

if __name__ == '__main__':
    print(solution(N = 512, K = 10))
    print(solution(N = 191, K = 4))
    print(solution(N = 285, K = 20))