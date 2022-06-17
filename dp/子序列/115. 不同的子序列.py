# -*- coding:utf-8 -*-
"""

编辑序列的问题
 难点在于构造递推公式
 分成两种情况：
 s[i-1] == t[j-1]
 当相等的时候，还要分成，是否使用s[i-1]
https://github.com/skywak3r/leetcode-master/blob/master/problems/0115.%E4%B8%8D%E5%90%8C%E7%9A%84%E5%AD%90%E5%BA%8F%E5%88%97.md
"""

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] *(len(t)+1) for _ in range(len(s)+1)]
        for i in range(len(s)):
            dp[i][0] = 1
        for j in range(1, len(t)):
            dp[0][j] = 0


        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[-1][-1]