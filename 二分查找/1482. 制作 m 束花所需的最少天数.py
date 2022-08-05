# -*- coding:utf-8 -*-
"""

单调，递增


"""


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def getDay(bloomDay, mid, k):
            # mid天，相邻k 可以返回几朵花
            count = 0
            tmp = [max((num - mid),0) for num in bloomDay  ]
            # print(tmp)
            index = 0
            cur = 0
            while index < len(bloomDay):
                if tmp[index] == 0:
                    cur += 1
                    if cur == k:
                        count += 1
                        cur = 0
                else:
                    cur = 0
                index += 1
            return count
        if m * k > len(bloomDay):
            return -1
        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            count = getDay(bloomDay, mid,k)
            if count < m:
                left = mid + 1
            else:
                right = mid
        return left

