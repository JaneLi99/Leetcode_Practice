def levelOrder(root):
    if len(root) == 0:
        return []
    if len(root) == 1:
        return [root]

    i = 0
    res = []
    list_num = 0
    while i < len(root):
        length = pow(2, list_num)
        res.append(root[i: i + length])
        list_num = list_num + 1
        i = i + length

    # Remove "None" in list
    for sub in res:
        j = 0
        while j < len(sub):
            if sub[j] == None:
                sub.remove(sub[j])
            else:
                j = j + 1
    return res

# Solution with TreeNode
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        queue = [root]
        next_queue = []
        level = []
        result = []
        while queue != []:
            for root in queue:
                level.append(root.val)
                if root.left is not None:
                    next_queue.append(root.left)
                if root.right is not None:
                    next_queue.append(root.right)
            result.append(level)
            level = []
            queue = next_queue
            next_queue = []
        return result

if __name__ == '__main__':
    print(levelOrder(root = [3, 9, 20, None, None, 15, 7]))
    print(levelOrder(root = [1]))
    print(levelOrder(root = []))