# -*- coding:utf-8 -*-
"""
1. 不关心如何走到，如果是障碍，那么直接这个点的dp为0就好
2. 在初始化的时候，如果边界上的点是障碍，后方的点 应该一律为0

"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0 for _ in range(n)] for __ in range(m)]
        for i in range(m):
            dp[i][0] = 1
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
                break
        for j in range(n):
            dp[0][j] = 1
            if obstacleGrid[0][j] == 1:
                dp[0][j] = 0
                break
        for i in range(1, m):
            for j in range(1, n):

                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0

        return dp[m - 1][n - 1]