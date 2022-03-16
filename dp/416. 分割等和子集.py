# -*- coding:utf-8 -*-
"""
分割问题建模称为 求容量为 sum/2的背包问题
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        numSum = sum(nums)
        if numSum %2 == 1:
            return False
        # nums.sort()
        target = numSum>>1
        # print(target)
        dp = [0 for _ in range(target+1)]
        for i in range(len(nums)):
            for j in range(target, nums[i]-1,-1):
                # print(j)
                dp[j] = max(dp[j],dp[j-nums[i]]+nums[i])
        # print(dp)
        return dp[target] == target