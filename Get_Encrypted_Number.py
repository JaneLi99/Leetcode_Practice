"""
Amazon OA 1 - Get Encrypted Number
In order to ensure maximum security, the developers at Amazon employ multiple encryption methods to keep user data protected.

In one method, numbers are encrypted using a scheme called 'Pascal Triangle'. When an array of digits is fed to this system,
it sums the adjacent digits. It then takes the rightmost digit (least significant digit) of each addition for the next step.
Thus, the number of digits in each step is reduced by 1. This procedure is repeated until there are only 2 digits left,
and this sequence of 2 digits forms the encrypted number.

Given the initial sequence of the digits of numbers, find the encrypted number. You should reort a string of digits representing
the encrypted number.

Example:
number = [4, 5, 6, 7]
Encryption occurs as follows:
4 + 5 + 6 + 7
  9 + 11 + 13
    20 + 24
      0 4
"""

def getEncryptedNumber(numbers):
    for i in range(len(numbers)):
        if numbers[i] > 10:
            return ""

    if len(numbers) == 2:
        res = str(numbers[0]) +  str(numbers[1])
        return res

    sum = []
    while len(sum) != 2:
        sum = []
        for i in range(len(numbers) - 1):
            two_sum = (numbers[i] + numbers[i + 1]) % 10
            sum.append(two_sum)
        numbers = sum

    if len(sum) == 2:
        res = str(sum[0]) + str(sum[1])
        return res

if __name__ == '__main__':
    print(getEncryptedNumber(numbers = [4, 5, 6, 7]))
    print(getEncryptedNumber(numbers = [0, 0]))
    print(getEncryptedNumber(numbers = [12, 13]))