# -*- coding:utf-8 -*-

"""
把问题转化为自己会的问题：
正常遍历。
如果方向改变，append 倒序即可


"""


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:    return []
        ans, queue,direction = [],collections.deque(),1
        queue.append(root)
        while queue:
            tmp = []
            for i in range(len(queue)):
                cur = queue.popleft()
                tmp.append(cur.val)
                if cur.left:    queue.append(cur.left)
                if cur.right:   queue.append(cur.right)
            if direction > 0:
                ans.append(tmp)
            else:
                ans.append(tmp[::-1])
            direction *= -1
        return ans




