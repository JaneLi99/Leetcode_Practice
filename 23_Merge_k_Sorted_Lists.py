# Very simple solution when lists is a list instead of listnode
def mergeKLists(lists):
    mergelist = []
    for i in range(len(lists)):
        mergelist = mergelist + lists[i]
    return mergelist

# Solution with Linkedlist
def mergeKLists_linkedlist(lists):
    if not lists or len(lists) == 0:
        return None
    while len(lists) > 1:
        mergedList = []

        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            mergedList.append(mergeList(l1, l2))
        lists = mergedList
    return lists[0]

def mergeList(l1, l2):
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
    return dummy.next


if __name__ == '__main__':
    mergeKLists([[1,4,5],[1,3,4],[2,6]])
    mergeKLists([])
    mergeKLists([[]])