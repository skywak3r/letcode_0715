# -*- coding:utf-8 -*-
"""
贪心：以一天为单位， 如果能赚，就赚  不能赚就不加
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum([prices[i+1]-prices[i] for i in range(len(prices)-1) if prices[i+1]-prices[i] > 0])

"""
"""
dp



"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 2 for _ in range(len(prices))]
        if len(prices) == 0:
            return 0
        dp[0][0] = -prices[0]
        dp[0][1] = 0

        for i in range(1,len(prices)):
            dp[i][0] = max( dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        # print(dp)
        return dp[-1][1]