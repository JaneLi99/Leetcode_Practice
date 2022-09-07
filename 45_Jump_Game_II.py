def jump(nums):
    jumps = 0
    jumpMaxIdx = 0
    nextJumpMaxIdx = 0

    for i, num in enumerate(nums):
        print(i, num)
        if jumpMaxIdx < i:
            jumps += 1
            jumpMaxIdx = nextJumpMaxIdx

        nextJumpMaxIdx = max(nextJumpMaxIdx, i + num)

    return jumps

if __name__ == '__main__':
    print(jump(nums = [2,3,1,1,4]))
    print(jump(nums = [2,3,0,1,4]))