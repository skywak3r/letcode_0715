# -*- coding:utf-8 -*-
"""
先写出汉语的意思，再翻译成程序语言

如果head 和head。next是空的。那就返回head

交换head 和head。next

head。next = 把 head。next翻转的结构



"""

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        newHead = head.next
        tmp = newHead.next
        newHead.next = head
        head.next = self.swapPairs(tmp)
        return newHead