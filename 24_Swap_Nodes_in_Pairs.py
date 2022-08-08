# Solution by using List
def swapPairs(head):
    if len(head) <= 1:
        return head
    res = []
    if len(head) % 2 == 0:
        for i in range(0, len(head), 2):
            res.append(head[i + 1])
            res.append(head[i])
    else:
        for i in range(0, len(head) - 1, 2):
            res.append(head[i + 1])
            res.append(head[i])
        res.append(head[len(head) - 1])
    return res

# Solution by using ListNode
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            # save ptrs
            nextPair = curr.next.next
            second = curr.next

            # reverse this pair
            second.next = curr
            curr.next = nextPair
            prev.next = second

            # update ptrs
            prev = curr
            curr = nextPair

        return dummy.next

if __name__ == '__main__':
    print(swapPairs(head = [1,2,3,4,5]))
    print(swapPairs(head = []))
    print(swapPairs(head = [1]))