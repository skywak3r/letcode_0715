# -*- coding:utf-8 -*-
"""
重要： 1.使用set去存储当前dfs已经遍历过的地方，去节省空间，否则会调用太多次dfs
2. possible的时候要一步一步来
3. 求二维数组的最大值的时候，写错了r = max(max([row for row in grid]))  这样会求到数组的第一列最大的数字


"""


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # r = max(max([row for row in grid]))
        # l = 0
        l, r = 0, max([max(vec) for vec in grid])

        n = len(grid)
        seen = set()

        def possible(mid, i, j):
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] > mid:
                return False
            if i == n - 1 and j == n - 1:
                return True
            if (i, j) in seen:
                return False
            seen.add((i, j))
            return possible(mid, i, j + 1) or possible(mid, i + 1, j) or possible(mid, i, j - 1) or possible(mid, i - 1,
                                                                                                             j)

        while l <= r:
            mid = (l + r) >> 1
            if possible(mid, 0, 0):
                r = mid - 1
            else:
                l = mid + 1
            seen = set()

        return l

