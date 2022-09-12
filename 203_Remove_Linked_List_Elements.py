# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head, val):
        ret = cursor = ListNode(0, head)

        while cursor and cursor.next:
            if cursor.next.val == val:
                cursor.next = cursor.next.next
            else:
                cursor = cursor.next

        return ret.next

solution = Solution()
print(solution.removeElements(head = [1,2,6,3,4,5,6], val = 6))
print(solution.removeElements(head = [], val = 1))
print(solution.removeElements(head = [7,7,7,7], val = 7))