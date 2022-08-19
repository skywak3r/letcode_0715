# -*- coding:utf-8 -*-
"""
思想：
写出面积计算公式。
用双指针，每次移动较小的那一个边往内部走


"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) -1
        res = 0
        while l < r :
            area = (min(height[l], height[r]) * (r - l))
            res = max(res, area)
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return res
