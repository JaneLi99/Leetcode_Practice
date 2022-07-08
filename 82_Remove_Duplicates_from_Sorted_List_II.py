# Solution with List
def deleteDuplicates(head):
    rm_d = []
    for i in range(len(head)):
        if head[i] not in rm_d:
            rm_d.append(head[i])
    d = [i for i in rm_d if not i in head or head.remove(i)]
    res = [j for j in rm_d if not j in head or head.remove(j)]
    return res

# Solution with LiseNode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0, next = head)
        slow = dummy

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                slow.next = head.next
            else:
                slow = slow.next
            head = head.next

        return dummy.next

if __name__ == '__main__':
    print(deleteDuplicates(head = [1,2,3,3,4,4,5]))
    print(deleteDuplicates(head = [1,1,1,2,3]))
