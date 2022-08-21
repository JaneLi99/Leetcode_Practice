import itertools
import math

def reorderedPowerOf2(n):
    if len(str(n)) == 1:
        res = math.log(n, 2)
        return res.is_integer()

    num_list = [i for i in str(n)]
    for num_tuple in itertools.permutations(num_list):
        if num_tuple[0] != "0":
            num = int(''.join(num_tuple))
            res = math.log2(num)
            if res.is_integer() == False:
                continue
            else:
                return True
    return False

if __name__ == '__main__':
    print(reorderedPowerOf2(n = 1))
    print(reorderedPowerOf2(n = 10))
    print(reorderedPowerOf2(n = 1420))
    print(reorderedPowerOf2(n = 597))