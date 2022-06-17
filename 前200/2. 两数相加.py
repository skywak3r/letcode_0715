# -*- coding:utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def getNum(node):
            if not node:
                return 0
            i = 0
            tmp = 0
            nums = 0
            while node:
                tmp = node.val
                nums += tmp * 10 ** i
                node = node.next
                i += 1
            return nums

        def splitNum(num):
            src = []
            if num == 0:
                src.append(0)
                return src
            while num:
                tmp = num % 10
                num = num // 10
                src.append(tmp)
            return src

        def constructList(nums):
            if len(nums) == 0:
                return None
            dummy = ListNode()
            cur = dummy
            for i in range(len(nums)):
                cur.next = ListNode(nums[i])
                cur = cur.next
            return dummy.next

        num1 = getNum(l1)

        num2 = getNum(l2)
        num = num1 + num2
        tmp = splitNum(num)
        return constructList(tmp)

