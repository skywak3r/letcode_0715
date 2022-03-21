# -*- coding:utf-8 -*-
"""
记忆化递归
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)

        def dfs(amount):
            if amount<0:
                return float('inf')
            if amount == 0:
                return 0
            ans = float('inf')
            for coin in coins:
                ans = min(ans, dfs(amount-coin)+1)
            return ans
        ans = dfs(amount)
        return -1 if ans == float('inf') else ans

#完全背包问题：
1. 可以重复取
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1 ] *(amount+1)
        dp[0] = 0

        for coin in coins:
            for j in range(coin, amount+1):
                dp[j] = min(dp[j], dp[j-coin]+1)

        return dp[amount] if dp[amount]<amount+1 else -1


"""
"""
dp
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] = min(dp[x], dp[x-coin]+1 )
        return dp[amount] if dp[amount] != float('inf') else -1

"""