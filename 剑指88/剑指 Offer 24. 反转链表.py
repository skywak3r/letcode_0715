# -*- coding:utf-8 -*-
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        fomer, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = fomer
            fomer = cur
            cur = tmp
        return fomer



"""
递归

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        fomer, cur = None, head
        def rever(pre, head):
            if not head:
                return pre
            res = rever(head, head.next)
            head.next = pre
            return res 

        return rever(fomer, head)
        
        https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/solution/kan-bu-dong-di-gui-de-kan-guo-lai-xi-wan-1akq/
"""