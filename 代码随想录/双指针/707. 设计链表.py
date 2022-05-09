# -*- coding:utf-8 -*-
""""""
"""
pre = dummy 
用pre控制

"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.dummyNode = Node(-1)
        self.length = 0

    def get(self, index: int) -> int:
        if 0 <= index < self.length:
            cur = self.dummyNode
            for i in range(index + 1):
                cur = cur.next
            return cur.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        # tmp = self.dummyNode.next
        # newNode = Node(val)
        # self.dummyNode.next = newNode
        # newNode.next = tmp
        # self.length += 1

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.length, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return

        # [so weird] If index is negative,
        # the node will be inserted at the head of the list.
        if index < 0:
            index = 0

        self.length += 1
        # find predecessor of the node to be added
        pred = self.dummyNode
        for _ in range(index):
            pred = pred.next

        # node to be added
        to_add = ListNode(val)
        # insertion itself
        to_add.next = pred.next
        pred.next = to_add

        # if index < 0 :
        #     index = 0
        # if index > self.length:
        #     return
        # newNode = Node(val)
        # pre = self.dummyNode
        # for i in range(index):
        #     pre = pre.next
        # newNode.next = pre.next
        # pre.next = newNode
        # # newNode.next = cur
        # self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self.length:
            self.length -= 1
            pre = self.dummyNode
            for _ in range(index):
                pre = pre.next
                # pre, cur = cur, cur.next
            pre.next = pre.next.next

# # Your MyLinkedList object will be instantiated and called as such:
# # obj = MyLinkedList()
# # param_1 = obj.get(index)
# # obj.addAtHead(val)
# # obj.addAtTail(val)
# # obj.addAtIndex(index,val)
# # obj.deleteAtIndex(index)