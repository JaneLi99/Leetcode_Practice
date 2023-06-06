def canMakeArithmeticProgression(arr):
    if len(arr) <= 2:
        return True

    arr.sort()
    diff = arr[1] - arr[0]
    clk = 0
    for i in range(2, len(arr)):
        if arr[i] - arr[i - 1] == diff:
            clk += 1
    if clk == len(arr) - 2:
        return True

    return False


if __name__ == '__main__':
    print(canMakeArithmeticProgression(arr = [3,5,1]))
    print(canMakeArithmeticProgression(arr = [1,2,4]))
