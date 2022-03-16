# -*- coding:utf-8 -*-
"""
二叉搜索树：左子树都小于根节点，根节点都小于右子树

中序遍历是有序的顺序。
    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            if not node:
                return []
            if node.left:
                inorder(node.left)
            res.append(node.val)
            if node.right:
                inorder(node.right)
        res = []
        inorder(root)
        return res[k-1]

"""

#迭代
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return
        cur, stack = root, []
        res = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res[k - 1]




