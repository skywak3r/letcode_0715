# -*- coding:utf-8 -*-
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        cur = head
        length = 1
        while cur:
            cur = cur.next
            length += 1
        cur = head
        count = 1
        while cur :
            if count == length -k:
                break
            cur = cur.next
            count += 1

        return cur

"""
快慢指针

设置两个指针， 第一个指针先走k步

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        former, later = head, head
        for i in range(k):
            former = former.next
        while former:
            former, later = former.next, later.next
        return later

"""