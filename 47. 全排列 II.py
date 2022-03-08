# -*- coding:utf-8 -*-

"""


一般sort一下
回溯问题的三要素：
有效结果
回溯条件 答案更新
剪枝

"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        src = []
        path = []
        length = len(nums)
        nums.sort()
        used = [False for _ in range(length)]
        def backtrack(nums, used,begin):
            if len(path) == len(nums):
                src.append(path[:])
            for i in range(begin, len(nums)):
                if used[i]:
                    continue
                if i>0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                path.append(nums[i])
                used[i] = True
                backtrack(nums, used,begin)
                used[i] = False
                path.pop()
        backtrack(nums,used,0)
        return src