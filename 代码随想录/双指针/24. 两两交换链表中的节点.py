# -*- coding:utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
""""""
"""
双指针用pre控制比较方便
画图
"""

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        while pre.next and pre.next.next:
            cur = pre.next
            post = cur.next

            cur.next = post.next
            pre.next = post
            post.next = cur
            pre = pre.next.next

        return dummy.next

