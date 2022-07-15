# -*- coding:utf-8 -*-
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)

"""
排序数组中的搜索问题，首先想到 二分法 解决。

"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        l, r = 0, len(nums)
        while l < r:
            mid = l + (r-l) // 2
            if nums[mid] == mid :
                l = mid + 1
            else:
                r = mid
        return l