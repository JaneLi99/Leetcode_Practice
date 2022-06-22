def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    bracket_map = {"(": ")", "[": "]", "{": "}"}
    open_par = set(["(", "[", "{"])
    stack = []
    for i in s:
        if i in open_par:
            stack.append(i)
        elif stack and i == bracket_map[stack[-1]]:
            stack.pop()
        else:
            return False
    return stack == []

if __name__ == '__main__':
    print(isValid("()"))
    print(isValid("()[]{}"))
    print(isValid("(]"))

    # Input: s = "()"
    # Output: true
    #
    # Input: s = "()[]{}"
    # Output: true
    #
    # Input: s = "(]"
    # Output: false