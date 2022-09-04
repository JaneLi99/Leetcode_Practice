"""
Cisco OA 1
The arithmetic mean of N number is the sum of the number, divided by N. The mode of N numbers is the most frequently
occuring number. Your program must output the mean and mode of a set of numbers.

Input
The first line of the input consists of an integer - inputArr_size, an integer representing the count of numbers in
the given list.
The second line of the input consists of N space-separated real numbers - inputArr representing the numbers of the
given list.

Output
Print two space-separated real numbers up-to two digits representing the mean and mode of a set of numbers.

Constraints
0 < inputArr_size < 10 ^ 3
-10 ^ 5 <= inputArr[i] <= 10 ^ 5; where i is representing the index of the inputArr.
0 <= i <= inputArr_size

Note
'0' and negative numbers are valid inputs. If more than one number has the same frequency, then choose the smallest
number as a mode.

Example
Input:
5
1 2 7 3 2
Output:
3.00 2.00
Explanation:
The first number is the mean of the input numbers and the second number is the mode. mean = (1 + 2 + 7 + 3 + 2) / 5 = 3.00
mode = 2 has the highest frequency so the mode is 2.00. So the output should be [3.00 2.00]
"""

import statistics
from collections import Counter
from itertools import groupby

def meanAndMode(inputArr):
    mean = statistics.mean(inputArr)
    mean = "{:.2f}".format(mean)
    # mode = statistics.mode(inputArr)
    # mode = "{:.2f}".format(mode)

    # Check multiple modes
    freqs = groupby(Counter(inputArr).most_common(), lambda x: x[1])
    mode_list = ["{:.2f}".format(val) for val, count in next(freqs)]
    mode = ' '.join(mode_list)

    return mean, mode

def main():
    inputArr = []
    inputArr_size = int(input())
    inputArr = list(map(float, input().split()))

    result = meanAndMode(inputArr)
    print(" ".join([str(res) for res in result]))

if __name__ == "__main__":
    main()