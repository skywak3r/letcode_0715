# -*- coding:utf-8 -*-

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m,n = len(s), len(t)

        i = j = 0
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == m

"""
dp编辑距离

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        dp = [[0] * (len(t)+1 ) for _ in range(len(s)+1)]

        # for i in range(1, len(t)+1):
        #     dp[0][i] = 1
        for i in range(1,len(s)+1):

            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = dp[i][j-1]
        # print(dp)
        return dp[-1][-1] == len(s)"""