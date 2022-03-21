# -*- coding:utf-8 -*-
"""
按照绝对值大小排序，把最大的改成正的，如果所有的都是正的了，将最小的那个乘 (-1)**k

"""

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums,key=abs, reverse = True)
        for i in range(len(nums)):
            if k>0 and nums[i] < 0 :
                nums[i] *= -1
                k -= 1
        if k > 0 :
            nums[-1] *= (-1) **k
        return sum(nums)