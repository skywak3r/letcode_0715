# -*- coding:utf-8 -*-
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        # used = [[False] * n for _ in range(m)]

        up, down, left, right = 0, m-1, 0, n-1
        while True:
            for y in range(left,right+1):
                ans.append(matrix[up][y])
            up += 1
            if up > down:
                break
            for x in range(up, down+1):
                ans.append(matrix[x][right])
            right -= 1
            if right < left:
                break
            for y in range(right,left-1, -1):
                ans.append(matrix[down][y])
            down -= 1
            if up > down:
                break
            for x in range(down,up-1,-1):
                ans.append(matrix[x][left])
            left += 1
            if right < left:
                break
        return ans
