# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head):
        crr = ListNode(0)
        crr.next = head

        l1  = []
        l2 = []

        while crr.next:
            l1.append(crr.next.val)
            crr = crr.next

        while head:
            l2.append(head.val)
            head = head.next

        return l1 == l2[::-1]