# -*- coding:utf-8 -*-
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        index = 0
        ans = float("inf")
        src = 0
        for i in range(len(nums)):
            src += nums[i]
            while src >= target:
                ans = min(i - index + 1, ans)
                src -= nums[index]
                index += 1
        return ans if ans != float("inf") else 0