# -*- coding:utf-8 -*-
"""
最大公约数的问题
"""


class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        if targetCapacity == 0:
            return True
        if jug2Capacity == 0:
            return jug1Capacity == targetCapacity
        if jug1Capacity == 0:
            return jug2Capacity == targetCapacity

        smaller = min(jug1Capacity, jug2Capacity)
        while smaller:
            if jug1Capacity % smaller == 0 and jug2Capacity % smaller == 0:
                break
            smaller -= 1
        return targetCapacity % smaller == 0
