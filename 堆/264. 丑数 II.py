# -*- coding:utf-8 -*-

#用hash表存储已经存在的数字
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        factors = [2, 3, 5]
        heap = [1]
        heapq.heapify(heap)
        seen = {1}

        for i in range(n - 1):
            cur = heapq.heappop(heap)
            for factor in factors:
                if (nxt := cur * factor) not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)

        return heapq.heappop(heap)


