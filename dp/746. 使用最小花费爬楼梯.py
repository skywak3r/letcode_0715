# -*- coding:utf-8 -*-
"""
初始化很重要
https://leetcode-cn.com/problems/min-cost-climbing-stairs/solution/yi-bu-yi-bu-tui-dao-dong-tai-gui-hua-de-duo-chong-/

"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for _ in range(len(cost))]
        # dp[-1]=0
        dp[1] = min(cost[0],cost[1])
        for i in range(2,len(cost)):
            dp[i] =min(dp[i-2]+cost[i-1],dp[i-1]+cost[i])
        # print(dp)
        return dp[-1]



