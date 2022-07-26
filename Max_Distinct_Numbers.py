"""
Google OA 2

There is an array A consisting of N two-digit numbers.
You can choose any number from the array and replace it with its reversed version.
You can apply this operation as many times as you want.
What is the maximum number of distinct numbers that can be created?

Write a function: class Solution { public static int solution(int[] A); } that, given an array of N integers,
returns the maximum number of distinct numbers that can be represented after reversing the order of any number of integers.

Examples:
Given A = [15, 21, 50, 50], the answer is 4.
You can reverse one of the numbers 50,
therefore obtaining array A = [15, 21, 5, 50].
Each number in the array is now distinct.

Given A = [21, 99, 99, 21, 12], the answer is 3.
There are 3 distinct numbers in the array.
Reversing any number will result in a number that already is in the array.
"""

def solution(A):
    list_reverse = []
    A = list(set(A))
    for i in range(len(A)):
        reverse_number = str(A[i])[::-1]
        list_reverse.append(int(reverse_number))
    list_all = list(set(list_reverse + A))

    if len(list_all) > len(A):
        return len(A) + 1
    else:
        return len(list_all)

if __name__ == "__main__":
    print(solution(A = [15, 21, 50, 50]))
    print(solution(A = [21, 99, 99, 21, 12]))
