import math

def powerfulIntegers(x, y, bound):
    if bound == 0:
        return []

    if x == 1:
        max_pow_x = 1
    else:
        max_pow_x = int(math.log(bound, x))

    if y == 1:
        max_pow_y = 1
    else:
        max_pow_y = int(math.log(bound, y))

    res = []
    for i in range(max_pow_x + 1):
        for j in range(max_pow_y + 1):
            sum = pow(x, i) + pow(y, j)
            if sum <= bound and sum not in res:
                res.append(sum)
    return res

if __name__ == '__main__':
    print(powerfulIntegers(x = 2, y = 1, bound = 10))
    print(powerfulIntegers(x = 3, y = 5, bound = 15))
    print(powerfulIntegers(x = 2, y = 3, bound = 0))