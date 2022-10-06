# -*- coding:utf-8 -*-
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(nums, path, index):
            res.append(path[:])
            if index >= len(nums):
                return
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(nums, path, i + 1)
                path.pop()

        backtrack(nums, path, 0)

        return res