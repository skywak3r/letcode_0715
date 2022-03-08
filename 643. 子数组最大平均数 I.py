# -*- coding:utf-8 -*-
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 0:
            return 0
        _sum, max_ava = 0, -inf
        start = 0
        cache = 0
        for end in range(len(nums)):
            _sum += nums[end]
            if end - start + 1 == k:
                max_ava = max(max_ava, _sum / k)

            if end >= k - 1:
                _sum -= nums[start]
                start += 1
        return max_ava


