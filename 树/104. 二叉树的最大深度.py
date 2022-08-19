# -*- coding:utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

"""
层序遍历

是用一个queue去模拟，每次pop出的是队头
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = 0
        queue = collections.deque()
        queue.append(root)

        while queue:
            length = len(queue)
            for i in range(length):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            level += 1
        return level

