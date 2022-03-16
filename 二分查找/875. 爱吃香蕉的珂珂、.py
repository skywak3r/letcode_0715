# -*- coding:utf-8 -*-
#


"""
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