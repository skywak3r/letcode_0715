# -*- coding:utf-8 -*-
"""


会做
"""

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def getWeight(weights, mid):
            count = 1
            index = 0
            curRemain = mid
            while index < len(weights):
                if curRemain - weights[index] >= 0:
                    curRemain -= weights[index]
                else:
                    curRemain = mid - weights[index]
                    count += 1
                index += 1
            return count

        left, right = max(weights), sum(weights)
        while left < right :
            mid = left + (right - left) // 2
            count = getWeight(weights, mid)
            if count > days:
                left = mid + 1
            else:
                right = mid

        return left
