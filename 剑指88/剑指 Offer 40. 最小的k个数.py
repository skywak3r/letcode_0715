# -*- coding:utf-8 -*-
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        src = []
        for i in range(len(arr)):
            heapq.heappush(src,arr[i])
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(src))
        return ans