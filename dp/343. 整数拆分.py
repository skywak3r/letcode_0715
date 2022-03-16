# -*- coding:utf-8 -*-
"""
note: 因为分解一个数，所以是一维的

1.dp[i]代表 拆分数字i之后的最大乘积
2。 dp[i] 由三部分组成   dp[i-j]j  j[i-j] dp[i]
3, 初始化

"""
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[2] = 1
        for i in range(3,n+1):
            for j in range(1,i-1):
                dp[i] = max(j*(i-j),j*dp[i-j],dp[i])
        return dp[-1]