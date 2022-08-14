# Solution O(n ^ 2)
def largestRectangleArea(heights):
    res = heights.copy()
    for i in range(len(heights)):
        for j in range(i + 1, len(heights)):
            height = min(heights[i : j + 1])
            width = abs(i - j) + 1
            area = height * width
            res.append(area)
    return max(res)

# More Efficient Solution
def largestRectangleArea_2(heights):
    stack, mx = [], 0
    for i,h in enumerate(heights + [0]):
        while stack and heights[stack[-1]] > h:
            H = heights[stack.pop()]
            if not stack:
                W = i
            else:
                W = i - stack[-1] - 1
            mx = max(mx, H * W)
        stack.append(i)
    return mx

if __name__ == '__main__':
    print(largestRectangleArea(heights = [2,1,5,6,2,3]))
    print(largestRectangleArea(heights = [2,4]))

    print(largestRectangleArea_2(heights=[2, 1, 5, 6, 2, 3]))
    print(largestRectangleArea_2(heights=[2, 4]))
