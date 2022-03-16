# -*- coding:utf-8 -*-
#递归
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(node):
            if not node:
                return []
            if node.left:
                postorder(node.left)
            if node.right:
                postorder(node.right)
            res.append(node.val)
            # postorder(node)
        res = []
        postorder(root)
        return res

"""
迭代
###
前序遍历的思路，先left 后right 最后翻转res即可

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack, cur = [], root
        res = []
        stack.append(cur)
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.left:
                stack.append(cur.left)
                
            if cur.right:
                stack.append(cur.right)
        return res[::-1]
            






"""