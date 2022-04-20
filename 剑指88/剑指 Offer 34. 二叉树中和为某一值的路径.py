# -*- coding:utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
backtrack
要先对当前的节点进行处理，
再去判断是否满足条件

如果是判断再去操作的话，
很可能已经满足条件了。刚好是叶子节点
但是进不去backtrack
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:

        ans = []
        path = []

        def backtrack(root, target, path):
            target -= root.val
            path.append(root.val)
            if target == 0 and not root.left and not root.right:
                ans.append(path.copy())

            if root.left:
                backtrack(root.left, target, path)
            if root.right:
                backtrack(root.right, target, path)
            path.pop()

        backtrack(root, target, path)
        return ans