# -*- coding:utf-8 -*-
"""
递归
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(Node):
            if not Node:
                return []
            if Node.left:
                inorder(Node.left)

            res.append(Node.val)
            if Node.right:
                inorder(Node.right)
        res = []
        inorder(root)
        return res


迭代


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:-
            return []
        stack = []
        res = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res



官方的

stack 不存
先将左边全压入
再访问当前


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        if not root:
            return
        res = []
        node = root
        stack = []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res
"""