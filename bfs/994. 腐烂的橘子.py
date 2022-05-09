# -*- coding:utf-8 -*-
""""""
"""
求
最短路径"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid),len(grid[0])
        count = 0
        queue = []
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))
        while queue and  count>0:
            ans += 1
            length = len(queue)
            for i in range(length):
                row, col = queue.pop(0)
                if row+1<m and grid[row+1][col] == 1:
                    grid[row+1][col] = 2
                    count -= 1
                    queue.append((row+1,col))
                if 0<=row-1 and grid[row-1][col] == 1:
                    grid[row-1][col] = 2
                    count -= 1
                    queue.append((row-1,col))
                if col+1<n and grid[row][col+1] == 1:
                    grid[row][col+1] = 2
                    count -= 1
                    queue.append((row,col+1))
                if col-1>=0 and grid[row][col-1] == 1:
                     grid[row][col-1] = 2
                     count -= 1
                     queue.append((row,col-1))
        if count>0:
            return -1
        else:
            return ans
