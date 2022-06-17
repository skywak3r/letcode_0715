# -*- coding:utf-8 -*-
"""
一共有四个状态，分别对4个状态 求出递推式。

"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0, 0, 0, 0] for _ in range(len(prices))]
        dp[0][1], dp[0][3] = -prices[0], -prices[0]
        if len(prices) < 2:
            return 0

        for i in range(1, len(prices)):
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
            dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])
        # print(dp)
        return dp[-1][4]