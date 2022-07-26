# Solution with using TreeNode
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def dfs(cur):
            if not cur:
                return None

            if cur == p or cur == q:
                return cur

            left = dfs(cur.left)
            right = dfs(cur.right)

            # first case
            if left and right:
                return cur

            # second case
            return left if left else right

        return dfs(root)

if __name__ == '__main__':
    print(lowestCommonAncestor(root = [3,5,1,6,2,0,8,None, None,7,4], p = 5, q = 1))
    print(lowestCommonAncestor(root = [3,5,1,6,2,0,8,None, None,7,4], p = 5, q = 4))
    print(lowestCommonAncestor(root = [1,2], p = 1, q = 2))