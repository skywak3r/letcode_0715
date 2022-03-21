# -*- coding:utf-8 -*-
"""
难点： 奇数偶数的控制， 尽量将其在循环中直接配置好，在赋值界面加减就好。
难点二： 将买卖股票3 进行拓展，奇数次为买入的时候，偶数次为卖出的时候。 有且仅有2k+1 中状态。所以直接枚举就好

"""
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[0] * (2 * k + 1) for _ in range(len(prices))]
        if len(prices) < 2:
            return 0
        for j in range(1, 2 * k, 2):
            dp[0][j] = -prices[0]
        # print(dp)
        for i in range(1, len(prices)):
            for j in range(0, 2 * k, 2):
                dp[i][j + 1] = max(dp[i - 1][j + 1], dp[i - 1][j] - prices[i])
                dp[i][j + 2] = max(dp[i - 1][j + 2], dp[i - 1][j + 1] + prices[i])
        # print(dp)
        return dp[-1][-1]