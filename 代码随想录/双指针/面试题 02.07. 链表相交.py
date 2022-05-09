# -*- coding:utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

""""""
"""
根据快慢法则，走的快的一定会追上走得慢的。
在这道题里，有的链表短，他走完了就去走另一条链表，我们可以理解为走的快的指针。

那么，只要其中一个链表走完了，就去走另一条链表的路。如果有交点，他们最终一定会在同一个
位置相遇
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur1, cur2 = headA, headB
        while cur1 != cur2:
            cur1 = cur1.next if cur1 else headB
            cur2 = cur2.next if cur2 else headA
        return cur1
