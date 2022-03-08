# -*- coding:utf-8 -*-
"""
数组法
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        src = [head]
        while src[-1].next:
            src.append(src[-1].next)
        return src[len(src) // 2]


"""
快慢指针，fast到达队尾，slow正好到达中间
"""