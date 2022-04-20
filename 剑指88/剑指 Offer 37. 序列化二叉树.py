# -*- coding:utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
层序遍历恢复和序列化二叉树。

返回字母形式

"""

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ans = []
        if not root:
            return "[]"
        stack = collections.deque()
        stack.append(root)
        while stack:
            cur = stack.popleft()
            if cur:
                ans.append(str(cur.val))
                stack.append(cur.left)
                stack.append(cur.right)
            else:
                ans.append("null")
        # print(ans )
        return "[" + ",".join(ans) + "]"

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "[]":
            return
        val, i = data[1:-1].split(","), 1
        root = TreeNode(int(val[0]))
        queue = collections.deque()
        queue.append(root)
        while queue:
            cur = queue.popleft()
            if val[i] != "null":
                cur.left = TreeNode(int(val[i]))
                queue.append(cur.left)
            i += 1
            if val[i] != "null":
                cur.right = TreeNode(int(val[i]))
                queue.append(cur.right)
            i += 1
        return root

    # Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))