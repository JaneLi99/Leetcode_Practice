def longestValidParentheses(s):
    stack = [-1]
    mx = 0
    for i, p in enumerate(s):
        if p == "(":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                mx = max(mx, i - stack[-1])
    return mx

# Another Solution


if __name__ == '__main__':
    print(longestValidParentheses(s = "(()"))
    print(longestValidParentheses(s = ""))
    print(longestValidParentheses(s = "(()())()))"))
    print(longestValidParentheses(s = ")()())()()("))