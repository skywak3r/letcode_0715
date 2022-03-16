# -*- coding:utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

###用一个标志位 判断正序入队或反序入队
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        cur, res = root, []
        tmp = []
        level = 1
        while queue:
            length = len(queue)
            for i in range(length):

                cur = queue[0]
                tmp.append(cur.val)
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
                queue = queue[1:]
            if level % 2:
                res.append(tmp)
            else:
                res.append(tmp[::-1])
            level += 1
            tmp = []
        return res