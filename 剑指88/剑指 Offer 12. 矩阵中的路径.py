# -*- coding:utf-8 -*-
"""
dfs岛屿问题：
想好dfs要返回什么东西

"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        used = [[False] * n for _ in range(m)]
        # count = 1
        # print(used)
        def dfs(i,j,k,used):
            if not 0<= i <m or not 0<=j <n or  used[i][j] or board[i][j] != word[k]:
                return False
            if k == len(word)-1:
                return  True
            used[i][j] = True
            ans = dfs(i, j + 1, k + 1, used) or dfs(i, j - 1, k + 1, used) or dfs(i + 1, j, k + 1, used) or dfs(i - 1, j,k + 1, used)
            used[i][j] = False
            return ans
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0,used):
                    return True
        return False

