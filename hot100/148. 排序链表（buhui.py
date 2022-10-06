# -*- coding:utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
https://leetcode.cn/problems/sort-list/solution/148-pai-xu-lian-biao-bottom-to-up-o1-kong-jian-by-/
自底向上的分治。
时间复杂度 nlogn. 空间复杂度 1

链表的三个技巧。
1. dummy node
2. cut
3. merge

"""
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        L= 0
        p = head
        while p:
            L += 1
            p = p.next
        dummyHead = ListNode(0)
        dummyHead.next = head
        step = 0
        while step < L:
            cur = dummyHead.next
            tail = dummyHead
            while cur:
                left = cur
                right = self.cut(left, step)
                cur = self.cut(right, step)
                tail.next = self.merge(left, right)
                while tail.next:
                    tail = tail.next
                step = step * 2 + 1
        return dummyHead.next
    def cut(self, head, step):
        """
        把head切step步， 返回切完后的值

        :param head:
        :param step:
        :return:
        """
        p = head
        while p and step:
            p = p.next
            step -= 1
        if not p:
            return None
        next = p.next
        p.next = None
        return next
    def merge(self, left, right):
        """
        合并两个有序链表
        :param left:
        :param right:
        :return:
        """
        dummyHead = ListNode(0)
        p = dummyHead
        while left and right:
            if left.val < right.val :
                p.next = left
                p = left
                left = left.next
            else:
                p.next = right
                p = right
                right = right.next
        p.next = left if left else right
        return dummyHead.next

