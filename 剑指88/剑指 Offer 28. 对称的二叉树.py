# -*- coding:utf-8 -*-
"""
递归三部曲：
1.返回值 和参数
2. 停止条件
3. 单层逻辑



class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def compare(left, right):
            if not left and not right:
                return True

            if left and right:
                if left.val == right.val:
                    out = compare(left.left,right.right)
                    inside = compare(left.right, right.left)
                    return out and inside
            return False

        return compare(root.left, root.right)

"""
"""
用栈

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = []
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            right = queue[-1]
            
            left = queue[-2]
            queue = queue[:-2]
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False


            queue.append(left.right)
            queue.append(right.left)
            queue.append(left.left)
            queue.append(right.right)

        return True
https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/solution/dui-cheng-er-cha-shu-di-gui-fa-die-dai-fa-xiang-ji/

"""