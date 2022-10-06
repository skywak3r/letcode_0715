# -*- coding:utf-8 -*-
"""
首先定义4个direction

首先写出递归树， 外层for循环是为了横轴的扫描



"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        DIRECTIONS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        visited = [[False] * n for _ in range(m)]

        def inArea(x, y):
            return 0 <= x < m and 0 <= y < n

        def backtrack(x, y, begin):
            if begin == len(word) - 1:
                return board[x][y] == word[begin]
            if board[x][y] == word[begin]:
                visited[x][y] = True
                for direction in DIRECTIONS:
                    newX = x + direction[0]
                    newY = y + direction[1]

                    if inArea(newX, newY) and not visited[newX][newY]:
                        if backtrack(newX, newY, begin + 1):
                            return True
                visited[x][y] = False
            return False
            # pass

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False




