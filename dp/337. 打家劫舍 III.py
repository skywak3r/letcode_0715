# -*- coding:utf-8 -*-
"""
暴力法：
思路就是:找规律，使用递归去维持堆栈，求出最大值。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        # def dfs(root):
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        val1 = root.val
        #使用根节点
        if  root.left:
            val1 += self.rob(root.left.left) + self.rob(root.left.right)
        if  root.right:
            val1 += self.rob(root.right.right)+self.rob(root.right.left)

        #不选根节点
        val2 = self.rob(root.right) + self.rob(root.left)

        return max(val1,val2)py
"""

"""
用hashmap存储已经遍历过的节点

class Solution:
    def __init__(self):
        self.seen =  defaultdict(int)
    def rob(self, root: TreeNode) -> int:
        # def dfs(root):
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        if self.seen == 0:
            return self.seen[root]
        print(self.seen)
        val1 = root.val
        #使用根节点
        if  root.left:
            val1 += self.rob(root.left.left) + self.rob(root.left.right)
        if  root.right:
            val1 += self.rob(root.right.right)+self.rob(root.right.left)

        #不选根节点
        val2 = self.rob(root.right) + self.rob(root.left)
        self.seen[root] = max(val1,val2)
        
        return max(val1,val2)
"""