# -*- coding:utf-8 -*-
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.defaultdict(int)
        for i in range(len(nums)):
            count[nums[i]] += 1
        heap = [(-c, num) for num,c in count.items()]
        heapq.heapify(heap)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans
