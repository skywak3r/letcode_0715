# -*- coding:utf-8 -*-
"""


"""
class Solution:
    def numSquares(self, n: int) -> int:

        squ = [i ** 2 for i in range(100)]
        dp = [n for _ in range(n + 1)]

        dp[0] = 0
        for i in range(1, n + 1):
            if squ[i] < n + 1:
                for j in range(squ[i], n + 1):
                    dp[j] = min(dp[j], dp[j - squ[i]] + 1)
            else:
                break
        print(dp)
        return dp[n]
