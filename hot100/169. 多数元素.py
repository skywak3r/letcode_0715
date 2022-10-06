# -*- coding:utf-8 -*-
"""
摩尔排序

众数是1 ，如果不是就-1


"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cadidate = None
        count = 0
        for num in nums :
            if count == 0:
                cadidate = num
            count += (1 if num == cadidate else -1 )
        return cadidate

