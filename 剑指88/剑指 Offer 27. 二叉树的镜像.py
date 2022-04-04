# -*- coding:utf-8 -*-

"""
二叉树的层序遍历

不熟练

"""

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        queue = []
        queue.append(root)
        while queue:
            cur = queue[0]
            queue = queue[1:]
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
            cur.left, cur.right = cur.right, cur.left
        return root


"""
递归发
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root 
        root.left, root.right = root.right, root.left
        root.left = self.mirrorTree(root.left)
        root.right = self.mirrorTree(root.right)
        return root                                                                



"""