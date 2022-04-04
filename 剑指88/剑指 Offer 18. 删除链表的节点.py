# -*- coding:utf-8 -*-


"""
判断特殊情况，要找特例测试

"""
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        pre, cur = None, head
        if head.val == val:
            return head.next
        while cur:

            if cur.val == val:
                if cur.next:
                    pre.next = cur.next

                    cur.next = None
                else:
                    pre.next = None
                return head
            pre = cur
            cur = cur.next
        return head