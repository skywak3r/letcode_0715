# -*- coding:utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
###主要是用inorder一分为二
#preorder是用于获取root
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        def dfs(inorder):
            x = preorder.pop(0)
            node = TreeNode(x)
            idx = inorder.index(x)
            leftInorder = inorder[:idx]

            rightInorder = inorder[idx + 1:]
            node.left = dfs(leftInorder) if leftInorder else None
            node.right = dfs(rightInorder) if rightInorder else None
            return node

        root = dfs(inorder)
        return root







