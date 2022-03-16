# -*- coding:utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # if head or head.next is None:
        #     return head
        smallHead, largeHead = ListNode(), ListNode()
        small, large, cur = smallHead, largeHead, head
        while cur:
            if cur.val < x:
                small.next = cur
                small = small.next

            else:
                large.next = cur
                large = large.next
            cur = cur.next

        small.next = largeHead.next
        large.next = None
        return smallHead.next