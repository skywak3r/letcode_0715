# -*- coding:utf-8 -*-
"""
方法一：正常岛屿问题
dfs 返回 是否满足条件
"""
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i<0 or j<0 or i>=m or j >= n :
                return False
            # print(i,j)
            if grid[i][j] == 1:
                return True
            else:
                if used[i][j]:
                    return True
                # print(i,j)
                used[i][j] = True
                down = dfs(i+1,j)
                up = dfs(i-1,j)
                left = dfs(i,j-1)
                right = dfs(i,j+1)
                return up and down and left and right
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        # print(f"m:{m},n:{n}")
        ans = 0
        used = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and not used[i][j]:
                    if dfs(i,j):
                        ans += 1
        # print(used)
        return ans
"""
方法2 ： 把边缘淹没，改变为岛屿问题
"""