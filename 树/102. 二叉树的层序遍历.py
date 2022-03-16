# -*- coding:utf-8 -*-
#核心思想，节点出队的时候，要将孩子节点入队。
"""

比普通的层序遍历多了一个【】，那就记录下当前的层的长度，用另外一个list 记录

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queen = [root]
        cur = root
        res = []
        tmp = []
        while queen:
            length = len(queen)
            for i in range(length):
                cur = queen[0]
                tmp.append(cur.val)
                if cur.left: queen.append(cur.left)
                if cur.right: queen.append(cur.right)
                queen = queen[1:]
            res.append(tmp)
            tmp = []
            # print(f"queen:{queen}")
            # print(f"res:{res}")
        return res



