# -*- coding:utf-8 -*-
"""
完全背包： 递推公式如下
for循环可以 调换， 且背包容量从小到大

"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1
        for i in range(len(coins)):
            for j in range(coins[i], amount+1):
                # print(i)
                dp[j] += dp[j-coins[i]]

        # print(dp)
        return dp[amount]