def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    # for i in range(len(list1)):
    #     list2.append(list1[i])
    # print(list2)
    #
    # for i in range(len(list2) - 1):
    #     for j in range(1, len(list2)):
    #         if list2[i] < list2[j]:

    if not list1: return list2
    if not list2: return list1

    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2

    return dummy.next

if __name__ == '__main__':
    print(mergeTwoLists([1, 2, 4], [1, 3, 4]))
    print(mergeTwoLists([], []))
    print(mergeTwoLists([], [0]))

    # Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
    # Output: [1, 1, 2, 3, 4, 4]
    #
    # Input: list1 = [], list2 = []
    # Output: []
    #
    # Input: list1 = [], list2 = [0]
    # Output: [0]