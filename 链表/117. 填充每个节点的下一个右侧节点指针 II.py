# -*- coding:utf-8 -*-
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = [root]
        while queue:
            length = len(queue)
            for i in range(length):
                cur = queue[0]
                if i == length - 1:
                    cur.next = None
                else:
                    # print(cur.val)

                    cur.next = queue[1]  # 本来是i+1 但是每次循环出队一个

                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
                queue = queue[1:]

        return root



