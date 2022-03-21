# -*- coding:utf-8 -*-
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if count > ans:
                ans = count
            if count <= 0:
                count = 0
        return ans
