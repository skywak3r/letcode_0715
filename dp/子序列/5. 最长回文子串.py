# -*- coding:utf-8 -*-
"""
回文问题直接用 dp解决
dp[i][j] i到j是否是回文串



"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1:
                        dp[i][j] = True
                    elif dp[i + 1][j - 1]:
                        dp[i][j] = True

        cur_length = 1
        cur_i, cur_j = -1, -1
        for i in range(len(s)):
            for j in range(len(s)):
                if dp[i][j]:
                    # print(i, j )
                    tmp = j - i + 1
                    if tmp > cur_length:
                        cur_length = tmp
                        cur_i, cur_j = i, j
        return s[cur_i:cur_j + 1] if cur_length > 1 else s[0]

