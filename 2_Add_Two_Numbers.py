
def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    if len(l1) > len(l2):
        len_range = len(l1) - len(l2)
        for i in range(len_range):
            l2.append(0)
    else:
        len_range = len(l2) - len(l1)
        for j in range(len_range):
            l1.append(0)

    output_list = [0]
    for i in range(len(l1)):
        if l1[i] + l2[i] + output_list[i] <= 9:
            output_list[i] = l1[i] + l2[i] + output_list[i]
            output_list.append(0)
        else:
            output_list[i] = l1[i] + l2[i] - 10 + output_list[i]
            output_list.append(1)

    last = len(output_list) - 1
    if output_list[last] == 0:
        output_list.remove(output_list[last])

    return output_list

    # Solution by using ListNode
    # dummy = ListNode()
    # cur = dummy
    #
    # carry = 0
    # while l1 or l2:
    #     v1 = l1.val if l1 else 0
    #     v2 = l2.val if l2 else 0
    #
    #     val = v1 + v2 + carry
    #
    #     carry = val // 10
    #     val = val % 10
    #     cur.next = ListNode(val)
    #
    #     cur = cur.next
    #     l1 = l1.next if l1 else None
    #     l2 = l2.next if l2 else None
    #
    # if carry > 0:
    #     cur.next = ListNode(val=1)
    #
    # return dummy.next


if __name__ == '__main__':
    print(addTwoNumbers([2, 4, 3], [5, 6, 4]))
    print(addTwoNumbers([0], [0]))
    print(addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9]))

    # Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
    # Output: [7, 0, 8]
    # Explanation: 342 + 465 = 807.
    #
    # Input: l1 = [0], l2 = [0]
    # Output: [0]
    #
    # Input: l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
    # Output: [8, 9, 9, 9, 0, 0, 0, 1]
