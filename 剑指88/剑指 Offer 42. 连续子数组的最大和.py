# -*- coding:utf-8 -*-


dp[i] 表示到nums【i 的最大前缀和

没写出来

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            if dp[i-1] > 0:
                dp[i] = dp[i-1]+nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)