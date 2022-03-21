# -*- coding:utf-8 -*-
"""
建模为：将石头分为尽可能相等的两部分-》将石头装入容量为sum/2的背包里面，最多能装多少

dp[sum/2] 就是容量为一半的背包装的最大价值
sum-dp[sum/2] 就是另外一堆的价值，并且肯定比dp[sum/2]要大。因为dp[sum/2]可能无法正好装下sum/2的价值

"""
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = [0] * 15001

        target = sum(stones) >> 1

        for i in range(len(stones)):
            for j in range(target, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
        # print(dp)
        return sum(stones) - dp[target] * 2