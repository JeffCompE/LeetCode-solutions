# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def reverse(head, k):
    prev = head
    cur = head.next
    head.next = None
    for i in range(k):
        next_ = cur.next
        cur.next = prev
        prev = cur
        cur = next_


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head

        head_ = head
        prev_k = None
        while head_:
            prev = head_
            tail_ = head_.next
            for i in range(k - 1):
                if tail_ is None:
                    reverse(prev, i)
                    return head
                next_ = tail_.next
                tail_.next = prev
                prev = tail_
                tail_ = next_

            tail_ = prev
            head_, tail_ = tail_, head_
            tail_.next = next_
            if prev_k:
                prev_k.next = head_
            else:
                head = head_
            prev_k = tail_
            head_ = next_
        return head
 
