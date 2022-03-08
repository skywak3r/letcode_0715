# -*- coding:utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
递归前序遍历
"""
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preOrder(Node):
            if not Node:
                return
            res.append(Node.val)
            preOrder(Node.left)
            preOrder(Node.right)

        res = []
        preOrder(root)
        return res

"""
迭代法

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        node = root
        stack = list()
        stack.append(root)
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if  node.right:
                stack.append(node.right)
            if  node.left:
                stack.append(node.left)
        return res


方法三：Morris 遍历


"""
