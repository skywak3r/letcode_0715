# -*- coding:utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
""""""
"""

"""

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # fast, slow = head, None
        # while fast:
        #     tmp = fast.next
        #     fast.next = slow
        #     slow = fast
        #     fast = tmp

        # return slow
        def reverse(pre, cur):
            if not cur:
                return pre
            tmp = cur.next
            cur.next = pre
            return reverse(cur, tmp)
        return reverse(None, head)