# Solution by using List
def reverseKGroup(head, k):
    if len(head) < k:
        return head
    res = []
    if len(head) % k == 0:
        for i in range(0, len(head), k):
            rev_sub = head[i: i + k]
            rev_sub.reverse()
            res = res + rev_sub
    else:
        remainder = len(head) % k
        for i in range(0, len(head) - remainder, k):
            rev_sub = head[i: i + k]
            rev_sub.reverse()
            res = res + rev_sub
        res = res + head[len(head) - remainder:]
    return res

# Solution by using ListNode
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # reverse group
            prev, curr = kth.next, groupPrev.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k = k - 1
        return curr

if __name__ == '__main__':
    print(reverseKGroup(head = [1,2,3,4,5,6], k = 3))
    print(reverseKGroup(head = [1,2,3,4,5], k = 2))