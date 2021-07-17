# # -*- coding:utf-8 -*-
# class Solution:
#     """
#     剑指offer 24题 翻转链表
#     以下为栈实现
#     还可以用双指针，递归
#     """
#     def reverseList(self, head: ListNode) -> ListNode:
#         s1 = []
#
#         while head != None:
#             s1.append(head)
#             head = head.next
#         if len(s1) == 0:
#             return None
#         firstHead = s1.pop()
#         newHead = firstHead
#         while len(s1) != 0:
#
#             newHead.next = s1.pop()
#             newHead = newHead.next
#             if len(s1) == 0:
#                 newHead.next = None
#
#         return firstHead
#
#
# """
# 双指针
# """
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         cur, pre = head, None
#         while cur:
#             tmp = cur.next # 暂存后继节点 cur.next
#             cur.next = pre # 修改 next 引用指向
#             pre = cur      # pre 暂存 cur
#             cur = tmp      # cur 访问下一节点
#         return pre
#


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or (head.next) == None :
            return head
        pre, cur = None, head
        # pre.next = None
        late = cur.next
        while cur!= None:
            cur.next = pre
            pre = cur

            if late == None:

                return cur
            cur = late
            late = late.next




if __name__ == "__main__":
    head = ListNode(10)
    tmp = ListNode(20)
    head.next = tmp
    res = Solution()
    head1 = res.reverseList(head)
    print(head1.next.next.val)
    # while head1 != None:
    #     print(head1.val)
    #     head1 = head1.next