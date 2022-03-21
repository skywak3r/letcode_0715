# -*- coding:utf-8 -*-
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        pre, cur = 0, 0
        res = 1
        for i in range(len(nums) - 1):
            cur = nums[i + 1] - nums[i]
            if cur * pre <= 0 and cur != 0:
                res += 1
                pre = cur
        return res

