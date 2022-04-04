# -*- coding:utf-8 -*-
"""

带层的层序遍历

"""


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque()
        queue.append(root)
        ans = []
        while queue:
            length = len(queue)

            tmp = []
            for i in range(length):
                cur = queue.popleft()
                tmp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            ans.append(tmp)

        return ans