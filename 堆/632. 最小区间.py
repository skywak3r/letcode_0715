# -*- coding:utf-8 -*-
"""
将k个一维数组转化为 矩阵。
1. 第二行构造矩阵的方式
2. 第四行构造最大值的方式
3. 使用堆维护矩阵中最小值，和他的横纵坐标
4.问题转化成了 从每个列表中取出一个数，使得最大的数-最小的数 最小
"""

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        l, r = -10**9, 10**9
        heap = [(row[0],i,0) for i, row in enumerate(nums)]
        heapq.heapify(heap)
        max_v = max(row[0] for row in nums)

        while True:
            min_v, row, col = heapq.heappop(heap)
            if r-l > max_v-min_v:
                l, r = min_v, max_v
            if col == (len(nums[row]) -1):
                return [l,r]
            heapq.heappush(heap,(nums[row][col+1],row,col+1))
            max_v = max(max_v, nums[row][col+1])
