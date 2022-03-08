# -*- coding:utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
方法一
链表转换成列表。

"""
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        src = list()
        node = head
        while node:
            src.append(node)
            node = node.next
        i, j = 0, len(src)-1

        while i < j:
            src[i].next = src[j]
            i += 1
            if i == j:
                break
            src[j].next = src[i]
            j -= 1
        src[i].next = None


"""
方法二：寻找链表中点 + 链表逆序 + 合并链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reorderList(self, head: ListNode) -> None:
        
        Do not return anything, modify head in-place instead.
    
        if not head or not head.next:
            return head        
        mid = self.findMid(head)
        cur = self.reverseList(mid)
        self.mergeList(head,cur)

    def findMid(self, head: ListNode) -> ListNode:

        slow, fast = head, head.next
        while fast:
            if not fast.next:
                mid = slow.next
                slow.next = None
                return mid
            slow = slow.next
            fast = fast.next.next
        mid = slow
        return mid
    def reverseList(self, node:ListNode)-> ListNode:
        if not node:
            return node
        pre, cur = None, node
        while cur:
            after = cur.next
            cur.next = pre
            pre = cur
            cur = after
        return pre
    def mergeList(self, head1:ListNode, head2:ListNode)->ListNode:
        while head1 and head2:
            tmp1 = head1.next
            tmp2 = head2.next
            head1.next = head2
            head2.next = tmp1
            head1 = tmp1
            head2 = tmp2





"""