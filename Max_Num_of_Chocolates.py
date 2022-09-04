"""
Cisco OA 2
There is a set of N jars. The jars contain differing numbers of chocolates. Some of the jars may be empty. Andrew may
pick multiple jars but he may not pick any jar that is adjacent to a jar that he has already picked.
Write a algorithm to calculate the maximum number of chocolates that Andrew may collect by picking jars.

Input
The first line of the input consists of an integer - choco_size, representing the number of jars of chocolates(N).
The second line of the input consists of N space-separated integers - choco, representing the number od chocolates in each jar.

output
Print an integer representing the maximum number of chocolates the Andrew may collect.

Contraints
1 < choco_size < 10 ^ 3
-10 ^ 5 <= choco[i] <= 10 ^ 5; where i is representing the index of the jars of chocolate.
0 <= i <= choco_size

Example
Input:
6
5 30 99 60 5 10
Output:
114
Explanation:
Andrew picks from the 1st(5), 3rd(99), and 6th jars (10).
"""

def maxNumOfChocolates(choco):
    if len(choco) == 1:
        return choco[0]

    dp = {}
    dp[0] = choco[0]
    dp[1] = max(choco[0], choco[1])
    for i in range(2, len(choco)):
        dp[i] = max(dp[i - 1], choco[i] + dp[i - 2])
    return max(dp.values())

def main():
    choco = []
    choco_size = int(input())
    choco = list(map(int, input().split()))

    result = maxNumOfChocolates(choco)
    print(result)

if __name__ == "__main__":
    main()