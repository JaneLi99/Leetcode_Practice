# Solution with List
def deleteDuplicates(head):
    res = []
    for i in range(len(head)):
        if head[i] not in res:
            res.append(head[i])
    return res

# Solution with LiseNode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        cur = head

        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head

if __name__ == '__main__':
    print(deleteDuplicates(head = [1,1,2]))
    print(deleteDuplicates(head = [1,1,2,3,3]))