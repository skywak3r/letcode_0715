# -*- coding:utf-8 -*-
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target+1)]
        dp[0] =1

        for weight in range(1,target+1):
            for num in nums:
                if weight>= num:
                    dp[weight] += dp[weight - num]
        # print(dp)
        return dp[target]