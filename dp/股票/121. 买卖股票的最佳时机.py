# -*- coding:utf-8 -*-
"""
贪心：
找到最小的值买入， 看后面的值是否能找到一个差值更大的
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        low = float('inf')
        for i in range(len(prices)):
            low = min(prices[i],low)
            ans = max(ans, prices[i] - low )
        return ans


"""
"""
dp[i][0] 第i天持有股票的金钱
dp[1][1]第i天卖出股票的钱
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 2 for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][1] = 0

        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(prices[i]+dp[i-1][0], dp[i-1][1])
        print(dp)
        return dp[-1][1]