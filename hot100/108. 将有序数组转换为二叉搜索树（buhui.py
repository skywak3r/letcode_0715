# -*- coding:utf-8 -*-
"""
每次把中间的数字作为根节点，区分左右子树


"""
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(nums, start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = dfs(nums, start, mid-1 )
            root.right = dfs(nums, mid+1, end)
            return root


        return dfs(nums, 0, len(nums)-1)