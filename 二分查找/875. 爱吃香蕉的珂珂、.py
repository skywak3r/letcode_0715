# -*- coding:utf-8 -*-
#


"""
最大值最小化的问题

根据题意可以知道：珂珂吃香蕉的速度越小，耗时越多。反之，速度越大，耗时越少，这是题目的 单调性；


在二分查找的基础上，加了一个possible函数
"""


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(mid):
            t = 0
            for pile in piles:
                t += (pile + mid - 1) // mid
            return t <= h

        l, r = 1, max(piles)

        while l <= r:
            mid = (r + l) >> 1
            if possible(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l


"""
二做

"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from math import ceil, floor
        left, right = 1, max(piles)
        def maxMin(nums, mid):
            count = 0
            for i in range(len(nums)):
                count += ceil(nums[i] / mid)  #向上取证
            # print(mid, count)
            return count
        while left < right:
            mid = left +  (right - left) // 2  # 左闭右开的区间
            count = maxMin(piles, mid)
            if count > h:
                left = mid + 1
            else:
                right = mid
        return left
