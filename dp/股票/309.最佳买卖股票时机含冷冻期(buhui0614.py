# -*- coding:utf-8 -*-
"""
难题：
难点1： 状态划分
难点2： 根据划分的状态 写出递推公式


1. 状态划分
（1） 状态1 ： 持有股票的收益
（2） 不持有股票的状态
    状态2：保持前天卖出的状态，当天不卖
    状态3： 今天卖出

（3） 状态4： 冷静期的收益

状态1：
dp[i][0]:
买入股票的来源：
1. 昨天就买了
2. 昨天是冷静期（状态4 或者没有卖股票（状态2。 我今天买.  max(dp[i-1][3] - prices[i], dp[i -1 ][1] - prices[i])
dp[i][0] = max(dp[i-1][0],  max(dp[i-1][3] - prices[i], dp[i -1 ][1] - prices[i]))

状态2：
当天不卖（已经度过冷静期）
来源：
1. 延续昨天不卖
2， 昨天是冷静期，
dp[i][1] = max(dp[i-1][1], dp[i-1][3])

状态3：
当天卖
来源：
只有一个来源： 我昨天持有股票
dp[i][2] = dp[i-1][0] + prices[i]

状态4：
冷静期
dp[i][3] = dp[i-1][2]
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        dp = [[0] * 4 for _ in range(len(prices))]
        for i in range(len(prices)):
            dp[i][0] = -prices[i]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], max(dp[i - 1][3] - prices[i], dp[i - 1][1] - prices[i]))
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][3])
            dp[i][2] = dp[i - 1][0] + prices[i]
            dp[i][3] = dp[i - 1][2]
        return max(dp[-1])