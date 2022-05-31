# -*- coding:utf-8 -*-
"""
1.dp[i] 从1到i构成的二叉搜索树的个数
2. dp[3] 包含 以1位节点的搜索数， 以2位节点的搜索树  以3为节点的搜索树

以3为节点的搜索树的数量： 左3乘右0  左2乘右1 左1乘右2
每个节点对应一个for循环

3.初始化
dp[]为什么设置 n+1维。
dp[n]表示为从1到n的搜索子树数量
dp[0] =
dp[1] =1




"""
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]

        # print(dp)
        return dp[-1]