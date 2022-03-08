# -*- coding:utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
###哈希表
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False




###快慢指针，快指针每次移动两步，慢指针移动一步，
###使用指针之前必须要判空
###
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next :
            return False
        slow = head
        fast = head.next

        while slow != fast:
            if not fast or  not fast.next:
                return False

            slow = slow.next
            fast = fast.next.next
        return True
