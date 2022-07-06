# Solution with using List
def removeNthFromEnd(head, n):
    index = len(head) - n
    head.remove(head[index])
    return head

# Solution with using Listnode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n: int):
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n = n - 1

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next

        return dummy.next

if __name__ == '__main__':
    print(removeNthFromEnd(head = [1,2,3,4,5], n = 2))
    print(removeNthFromEnd(head = [1], n = 1))
    print(removeNthFromEnd(head = [1,2], n = 1))
