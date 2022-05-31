# -*- coding:utf-8 -*-
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, curSum):
            if not root:
                return False
            if curSum - root.val == 0 and not root.left and not root.right:
                return True
            # print(root.val, curSum)
            return dfs(root.left, curSum - root.val) or dfs(root.right, curSum - root.val)
        return dfs(root, targetSum)