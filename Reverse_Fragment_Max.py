"""
Google OA 1

One fragment of a given integer N can be selected and its digits reversed (replaced with a right to left version of themselves).
What is the maximum number that can be obtained this way from integer N?

Write a function:
class Solution { public int solution(int N); } that, given an integer 1 <= N <= 1,000,000,000,
returns the greatest integer that can be created by reversing a subset of its digits.

Examples:
Given N = 5340, the answer is 5430. Fragment “34” can be reversed to "43".
Given N = 2043, the answer is 4023. Fragment “204” can be reversed to “402”.
Given N = 620, the answer is 620. There is no need to reverse any fragment.
"""

def solution(N):
    N = str(N)
    res = []
    for i in range(len(N) - 1):
        for j in range(i + 1, len(N)):
            new_N = N[0:i] + N[i:j + 1][::-1] + N[j + 1:]
            res.append(new_N)
    return max(res)

if __name__ == "__main__":
    print(solution(N = 54535))
    print(solution(N = 5340))
    print(solution(N = 2043))
    print(solution(N = 620))
