# Solution by using List
def reverseBetween(head, left, right):
    if len(head) == 1:
        return head
    new_left = head[right - 1]
    new_right = head[left - 1]

    res = []
    for i in range(len(head)):
        if i != left - 1 and i != right - 1:
            res.append(head[i])
        elif i == left - 1:
            res.append(new_left)
        elif i == right - 1:
            res.append(new_right)
    return res

# Solution by using ListNode
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head, left, right):
        dummy = ListNode(0, head)

        # 1. reach node at position "left"
        leftPrev, cur = dummy, head
        for i in range(left - 1):
            leftPrev, cur = cur, cur.next

        # Now cur = "left", leftPrev = "node before left"
        # 2. reverse from left to right
        prev = None
        for i in range(right - left + 1):
            tmpNext = cur.next
            cur.next = prev
            prev, cur = cur, tmpNext

        # 3. Update pointers
        leftPrev.next.next = cur  # cur is node after "right"
        leftPrev.next = prev  # prev is "right"
        return dummy.next

if __name__ == '__main__':
    print(reverseBetween(head = [1,2,3,4,5], left = 2, right = 4))
    print(reverseBetween(head = [5], left = 1, right = 1))
    print(reverseBetween(head=[1, 2, 3, 4, 5, 6, 7, 8], left=3, right=4))