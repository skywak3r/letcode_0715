# -*- coding:utf-8 -*-
""""""

"""
回溯的结束条件找错了。
按部就班成了ans append之后就要return

此处return应该是index走到最后了


而且因为此处题目要求是不相同的数组，所以不用seen判断重复
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        path = []
        ans = []
        # ans.append([])
        seen = set()
        def backtrack(path, index):
            if tuple(path) not in seen:
                ans.append(path[:])
                seen.add(tuple(path))
            if index >= len(nums):
                return
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(path, i + 1)
                path.pop()
        backtrack(path, 0)
        return ans