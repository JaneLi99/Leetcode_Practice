def hammingWeight(n):
    return (str(bin(n)).count('1'))

if __name__ == '__main__':
    print(hammingWeight(n =0o0000000000000000000000000001011))
    print(hammingWeight(n =0o0000000000000000000000010000000))
    print(hammingWeight(n = 11111111111111111111111111111101))