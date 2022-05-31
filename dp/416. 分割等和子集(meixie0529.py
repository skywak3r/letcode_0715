# -*- coding:utf-8 -*-
"""
分割问题建模称为 求容量为 sum/2的背包问题



0529 没写出
dp 的定义设置成了 dp[i] 是否能凑成i，

背包问题：
套到本题，dp[j]表示 背包总容量是j，最大可以凑成j的子集总和为dp[j]。


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