# -*- coding:utf-8 -*-
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row, column = m-1, 0

        while row >=0 and column < n:
            if matrix[row][column] > target:
                row -= 1
            elif matrix[row][column] < target:
                column += 1
            else:
                return True
        return False