from typing import List
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class minHeap:
    def __init__(self):
        self.arr = list()
        self.size = 0

    def heapify(self, i):
        l = 2 * i
        r = l + 1
        min_ = i
        if l < self.size and self.arr[min_].val > self.arr[l].val:
            min_ = l
        if r < self.size and self.arr[min_].val > self.arr[r].val:
            min_ = r
        if min_ != i:
            self.arr[min_], self.arr[i] = self.arr[i], self.arr[min_]
            self.heapify(min_)

    def push(self, node):
        self.size += 1
        self.arr.append(node)
        i = self.size - 1
        while i >= 1:
            parent = i // 2
            if parent >= 0 and self.arr[parent].val > self.arr[i].val:
                self.arr[parent], self.arr[i] = self.arr[i], self.arr[parent]
                i = parent
            else:
                break

    def pop(self):
        if self.size == 0:
            return None
        result = self.arr[0]
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        del self.arr[-1]
        self.size -= 1
        self.heapify(0)
        return result


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = minHeap()
        for node in lists:
            if node:
                heap.push(node)
        head = tail = heap.pop()
        if not head:
            return None
        if tail.next:
            heap.push(tail.next)
        while heap.size != 0:
            tail.next = heap.pop()
            tail = tail.next
            if tail.next:
                heap.push(tail.next)
        return head
