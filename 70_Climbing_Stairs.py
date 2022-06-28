def climbStairs(n):
    one = 1
    two = 1
    for i in range(n - 1):
        temp = one
        one = one + two
        two = temp
    return one


if __name__ == '__main__':
    print(climbStairs(2))
    print(climbStairs(3))
