# -*- coding:utf-8 -*-
"""
正确率 50/84
存在的问题：
1. 在排水的时候，没有按照在0后的顺序排水，

class Solution:
    def avoidFlood(self, rains) :
        length = len(rains)
        h = []
        ans = [0 for _ in range(length)]
        h = [(-rains.count(rain),rain ) for rain in set(rains)]
        heapq.heapify(h)
        # print(h)
        ans = [-1 for i in range(length)]
        for i in range(length):
            if rains[i] == 0:
                num, pos = heapq.heappop(h)
                num += 1
                heapq.heappush(h, (num, pos))
                # print(pos,num)
                ans[i] = pos
        num, pos = heapq.heappop(h)
        if num >= -1:
            # print(num)

            return ans
        else:
            return []

"""

"""
#时间太高了
1. 用二分查找找到需要泄洪的index



class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [1 for _ in range(len(rains))]
        sunny = []
        lakes = {}
        for i, rain in enumerate(rains):
            if rain > 0:
                ans[i] = -1
                if rain in lakes:
                    j = bisect.bisect_left(sunny, lakes[rain])
                    if j == len(sunny):
                        return []
                    ans[sunny.pop(j)] = rain

                lakes[rain] = i

            else:
                sunny.append(i)
        return ans 

"""
import heapq
from collections import defaultdict,deque

"""
遍历第一编 将每个lake下雨的天用dic 和列表存储
2. 用堆存放 最先需要被抽干的湖
"""
class Solution:
    def avoidFlood(self, rains) :
        water = defaultdict(deque)
        for i, lake in enumerate(rains):
            if lake != 0:
                water[lake].append(i)

        full = set()
        ans = []
        q = []
        for i, lake in enumerate(rains):
            if lake != 0:
                if lake in full:
                    return []
                else:
                    full.add(lake)
                    ans.append(-1)
                    water[lake].popleft()
                    if water[lake]:
                        heapq.heappush(q, water[lake][0])
            else:
                if not q:
                    ans.append(1)
                else:
                    index = heapq.heappop(q)
                    ans.append(rains[index])
                    full.remove(rains[index])
        return ans