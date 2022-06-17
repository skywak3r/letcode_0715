# -*- coding:utf-8 -*-
"""
dp[i[j 表示 word1 前i-1个  word2 前j-1个 相等的最小删除数

可以分为 word1 [i-1  和word2[j-1 是否相等  如果相等 就等 dp[i-1[j-1

不等的话就要删除， 删1还是2 还是都删
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word1)+1) for _ in range(len(word2)+1)]

        for i in range(len(word1)+1):
            dp[0][i] = i
        for j in range(len(word2)+1):
            dp[j][0] = j

        for i in range(1, len(word2)+1):
            for j in range(1, len(word1)+1):
                if word1[j-1] != word2[i-1]:
                    dp[i][j] = min([dp[i-1][j-1]+2, dp[i-1][j]+1, dp[i][j-1]+1])
                else:
                    dp[i][j] = dp[i-1][j-1]

        # print(dp)
        return dp[-1][-1]