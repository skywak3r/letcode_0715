# -*- coding:utf-8 -*-
#层序遍历 模板
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        queue = []
        cur = root
        queue.append(cur)
        length = len(queue)
        while queue:
            cur = queue.pop(0)
            ans = cur.val
            for i in range(length):
                if cur.right: queue.append(cur.right)
                if cur.left:  queue.append(cur.left)
        return ans
