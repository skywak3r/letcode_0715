# -*- coding:utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
因为是二叉搜索树， 所以可以直接根据数值判断。

有三种情况：
一种 q p 在root的左右子树下
2. q 是root  p在子树下面
3. 相反

保证 q > p 的情况下。 可以按照数值找到。


"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        while root:
            if root.val < p.val:
                root = root.right
            elif root.val > q.val:
                root = root.left
            else:
                break
        return root