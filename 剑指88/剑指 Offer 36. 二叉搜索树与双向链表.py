# -*- coding:utf-8 -*-
"""
中序遍历：
dfs(rigth)
xxx
dfs（left


双端列表：  pre.right,cur.left = cur,pre
        使用类的self保存pre


"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if self.pre:
                self.pre.right, root.left = root, self.pre
            else:
                self.head = root
            self.pre = root
            dfs(root.right)
        if not root:
            return
        self.pre = None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head