# -*- coding:utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        def reverseList(head: ListNode):
            pre, cur = None, head
            while cur:
                after = cur.next
                cur.next = pre
                pre = cur
                cur = after

        dummy_node = ListNode()
        dummy_node.next = head
        pre = dummy_node

        for i in range(left - 1):
            pre = pre.next
        begin = pre.next
        back = pre
        for i in range(right - left + 1):
            back = back.next
        end = back
        back = back.next
        end.next = None

        reverseList(begin)
        pre.next = end
        begin.next = back
        return dummy_node.next






