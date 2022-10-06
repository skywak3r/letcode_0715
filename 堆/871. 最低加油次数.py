# -*- coding:utf-8 -*-
"""
进入for循环之后 if语句判断的是特殊情况， 一般情况放在后面

"""
import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        cur_fuel = startFuel
        stations += [(target, 0)]
        h = []
        heapq.heapify(h)
        ans = 0
        last = 0
        for cur_pos, fuel in stations:
            cur_fuel = cur_fuel - (cur_pos - last)
            while cur_fuel < 0 and h:
                cur_fuel -= heapq.heappop(h)
                ans += 1
            if cur_fuel < 0:
                return -1
            else:
                heapq.heappush(h, -fuel)
                last = cur_pos
        return ans




