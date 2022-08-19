# -*- coding:utf-8 -*-
"""
dp是处理匹配问题的好办法。
难点在于 *的匹配

看题解把



"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        def is_match(i, j):
            if i == 0:
                return False
            if p[j-1] == ".":
                return True
            return s[i-1] == p[j-1]
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True
        for i in range(m+1):
            for j in range(1, n+1):
                if p[j-1] == "*":#难点
                    dp[i][j] |= dp[i][j-2]
                    if is_match(i, j-1):
                        dp[i][j] |= dp[i-1][j]
                else:
                    if is_match(i, j):
                        dp[i][j] |= dp[i-1][j-1]
        return dp[-1][-1]
