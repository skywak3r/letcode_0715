# -*- coding:utf-8 -*-
"""
一步一步往前走， 记录下当前一步能走到的最大范围， 如果走到了最大范围了。那么step + 1

"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        ans = 0
        curDistance = 0
        nextDistance = 0
        for i in range(len(nums)):
            nextDistance = max(nextDistance, nums[i] + i)

            if i == curDistance:
                curDistance = nextDistance
                ans += 1
                if nextDistance == len(nums):
                    break
        return ans
