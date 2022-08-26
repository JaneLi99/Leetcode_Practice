def reverseBits(n):
    ans = 0
    for i in range(32):
        b = (n >> i) & 1
        ans = ans | (b << (31 - i))
    return ans

if __name__ == '__main__':
    print(reverseBits(n =0o0000010100101000001111010011100))
    print(reverseBits(n = 11111111111111111111111111111101))