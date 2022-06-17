# -*- coding:utf-8 -*-

"""
dp[i]  表示以nums[i] 结尾的最长子序列
dp[i] 可由dp[j] 推导出来
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        # dp[0] = 1
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j] + 1)

        # print(dp)
        return max(dp)