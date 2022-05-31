# -*- coding:utf-8 -*-
""""""
"""
回溯的横向是列。纵向是行。 通过for循环控制列。递归 控制行。 每次填充一行。
1. 先判断是否有效 再去对其修改
2. isValid函数是否有效：
    因为是从上到下填充的，所以只需要判断对角线的左上和右上即可。
3. 对 行和列的控制 

"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        path = [["."] * n for _ in range(n)]
        # def isVaild(board,row, col):
        #     #判断同一列是否冲突
        #     for i in range(len(board)):
        #         if board[i][col] == 'Q':
        #             return False
        #     # 判断左上角是否冲突
        #     i = row -1
        #     j = col -1
        #     while i>=0 and j>=0:
        #         if board[i][j] == 'Q':
        #             return False
        #         i -= 1
        #         j -= 1
        #     # 判断右上角是否冲突
        #     i = row - 1
        #     j = col + 1
        #     while i>=0 and j < len(board):
        #         if board[i][j] == 'Q':
        #             return False
        #         i -= 1
        #         j += 1
        #     return True
        def isVaild(path, row, col ):
            for i in range(len(path)):
                if path[i][col] == "Q":
                    return False
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if path[i][j] == "Q":
                    return False
                i -= 1
                j -= 1
            i = row - 1
            j = col + 1
            while i >= 0 and j < len(path):
                if path[i][j] == "Q":
                    return False
                i -= 1
                j += 1
            return True
        def backtrack(path, row, n):
            if row == n:
                tmp = ["".join(line) for line in path]
                ans.append(tmp[:])
                return
            for i in range(n):
                if isVaild(path, row, i):
                    path[row][i] = "Q"
                    backtrack(path, row + 1, n)
                    path[row][i] = "."
        backtrack(path, 0, n)
        return ans