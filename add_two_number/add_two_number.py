# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        value = l1.val + l2.val
        carry = value // 10
        value = value % 10
        result = ListNode(value)
        cur_node = result

        l1 = l1.next
        l2 = l2.next

        while True:
            if l1 is None and l2 is None:
                if carry != 0:
                    new_node = ListNode(carry)
                    cur_node.next = new_node
                    cur_node = new_node
                break

            l1_val = 0 if l1 is None else l1.val
            l2_val = 0 if l2 is None else l2.val

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

            value = l1_val + l2_val + carry
            carry = value // 10
            value = value % 10
            new_node = ListNode(value)
            cur_node.next = new_node
            cur_node = new_node
        return result
       
