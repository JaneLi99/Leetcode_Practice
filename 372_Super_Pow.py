# Solution, but time limit exceeded
def superPow(a, b):
    power = int(''.join(map(str, b)))
    res = pow(a, power) % 1337
    return res

# Another Solution
class Solution:
    def superPow(self, a, b):
        if len(b) == 0:
            return 1
        templast = b[-1]
        b.pop(-1)
        part1 = self.mypow(a, templast)
        part2 = self.mypow(self.superPow(a, b), 10)
        return (part1 * part2) % 1337

    def mypow(self, num, k):
        if k == 0:
            return 1
        num = num % 1337

        if k % 2 == 0:
            res = self.mypow(num, int(k / 2))
            return (res * res) % 1337
        else:
            return (num * self.mypow(num, k - 1)) % 1337

if __name__ == '__main__':
    print(superPow(a = 2, b = [3]))
    print(superPow(a = 2, b = [1,0]))
    print(superPow(a = 1, b = [4,3,3,8,5,2]))
    print(superPow(a = 2, b = [1,2]))