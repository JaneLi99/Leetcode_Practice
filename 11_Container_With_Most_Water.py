def maxArea(height):

    # area_list = []
    # for i in range(len(height) - 1):
    #     for j in range(i + 1, len(height)):
    #         length = j - i
    #         width = min(height[j], height[i])
    #         area = length * width
    #         area_list.append(area)
    # max_area = max(area_list)
    # return max_area
    # O(n^2)

    result = 0
    l, r = 0, len(height) - 1
    while l < r:
        area = (r - l) * min(height[l], height[r])
        result = max(result, area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return result

if __name__ == '__main__':
    print(maxArea([1,8,6,2,5,4,8,3,7]))
    print(maxArea([1,1]))

