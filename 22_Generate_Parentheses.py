def generateParenthesis(n):

    def backtrack(s, left, right):
        if len(s) == 2 * n:
            res.add(s)
        if left < n:
            backtrack(s+'(', left + 1, right)
        if right < left:
            backtrack(s+')', left, right + 1)
    res = set()
    backtrack('', 0, 0)
    result = list(res)
    return result



if __name__ == '__main__':
    generateParenthesis(3)
    generateParenthesis(1)