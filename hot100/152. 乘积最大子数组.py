# -*- coding:utf-8 -*-
"""
注意初始化数组


"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxF = [0] * (len(nums) + 1)
        minF = [0] * (len(nums) + 1)

        for i in range(1, len(nums) + 1):
            maxF[i] = max(nums[i - 1] * maxF[i - 1], max(nums[i - 1], nums[i - 1] * minF[i - 1]))
            minF[i] = min(nums[i - 1] * minF[i - 1], min(nums[i - 1], nums[i - 1] * maxF[i - 1]))

        return max(maxF)