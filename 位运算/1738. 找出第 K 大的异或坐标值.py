# -*- coding:utf-8 -*-
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix),len(matrix[0])
        pre = [[0]*(n+1) for _ in range(m+1)]
        # print(m,n)
        result = []
        for i in range(1,m+1):
            for j in range(1,n+1):
                pre[i][j]= pre[i-1][j] ^ pre[i][j-1] ^pre[i-1][j-1]^ matrix[i-1][j-1]
                result.append(pre[i][j])
        result.sort(reverse=True)
        return result[k-1]
