# -*- coding:utf-8 -*-



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        while n > 0:
            fast = fast.next
            n -= 1
        slow = head
        pre = None
        while fast:
            pre = slow
            slow = slow.next
            fast = fast.next

        after = slow.next
        if pre:
            pre.next = after

        return head if pre else head.next
"""
快慢指针，先走n步，如果是头结点。那么久返回head.next 


"""


"""
dummy 控制更方便

"""

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        slow  = fast = dummy
        for i in range(n+1):
            fast = fast.next
        while fast:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return dummy.next