def checkPossibility(nums):
    changed = False

    for i in range(len(nums) - 1):
        if nums[i] <= nums[i + 1]:
            continue
        if changed:
            return False

        if i == 0 or nums[i + 1] >= nums[i - 1]:
            nums[i] = nums[i + 1]
        else:
            nums[i + 1] = nums[i]
        changed = True

    return True


if __name__ == '__main__':
    print(checkPossibility(nums = [4,2,3]))
    print(checkPossibility(nums = [4,2,1]))
    print(checkPossibility(nums = [3,4,2,3]))