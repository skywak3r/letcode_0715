# -*- coding:utf-8 -*-
"""
以每一天为单位，记录出所有赚钱的时候，
把所有赚钱的时候加起来，就是最大的收益

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = [0 for i in range(len(prices)-1)]
        for i in range(len(prices)-1):
            diff[i] = prices[i+1] - prices[i]
        ans = 0
        for i in range(len(diff)):
            if diff[i] > 0:
                ans += diff[i]
        return ans