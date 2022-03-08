# -*- coding:utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#深度优先搜索
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        def preord(root, target):

            if not root:
                return []
            path.append(root.val)
            target -= root.val    #一定要先append 在去遍历别人
            if not root.left and not root.right and target == 0:
                ret.append(path[:])

            preord(root.left, target)
            preord(root.right, target)
            path.pop()   #删除掉不满足的点

        ret, path = [], []##path是全局变量，所以不能放在内部
        preord(root, target)###target也是全局的，必须作为参数传递进去
        return ret

"""
广度优先搜索

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        src=[]
        path = []
        def dsf(root,target):
            if root is None:
                return 

            path.append(root.val)
            target -= root.val

            if (not root.left)  and( not root.right  )and target == 0:
                # print(f"target:{target}")
                src.append(path.copy())
                #返回
            # print(f"path:{path}")
            dsf(root.left, target)
            dsf(root.right, target)
            path.pop()

        dsf(root, target)
        return src
"""