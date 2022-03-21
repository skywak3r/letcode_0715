# -*- coding:utf-8 -*-
"""
完全背包问题

这个是排列问题的背包问题： 先遍历重量，在遍历价值



class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        dp[0] =1
        for i in range(n+1):
            for step in range(1,3):
                if i >= step:
                    dp[i] += dp[i-step]
        return dp[n]


"""


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        dp[0]=1
        for i in range(1,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]