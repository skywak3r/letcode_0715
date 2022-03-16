# -*- coding:utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        maxLen = 0

        def dfs(root, direction, length):

            if not root:
                return 0
            nonlocal maxLen
            maxLen = max(length, maxLen)

            if direction > 0:
                dfs(root.left, -direction, length + 1)
                dfs(root.right, direction, 1)
            else:
                dfs(root.right, -direction, length + 1)
                dfs(root.left, direction, 1)

        dfs(root, 1, 0)
        dfs(root, -1, 0)
        return maxLen


