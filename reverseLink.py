# -*- coding:utf-8 -*-
class Solution:
    """
    剑指offer 24题 翻转链表
    """
    def reverseList(self, head: ListNode) -> ListNode:
        s1 = []

        while head != None:
            s1.append(head)
            head = head.next
        if len(s1) == 0:
            return None
        firstHead = s1.pop()
        newHead = firstHead
        while len(s1) != 0:

            newHead.next = s1.pop()
            newHead = newHead.next
            if len(s1) == 0:
                newHead.next = None

        return firstHead