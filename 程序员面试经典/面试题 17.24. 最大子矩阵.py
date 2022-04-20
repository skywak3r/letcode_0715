# -*- coding:utf-8 -*-
"""
从1维点缀和 拓展到2维。
"""


class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        if m == 0:
            return [0,0,0,0]
        n = len(matrix[0])
        preSum = [0] * n
        ans = [0,0,0,0]
        maxSum = float("-inf")
        for i in range(m):
            preSum = [0] * n
            for j in range(i,m):
                sumMatrix = 0
                for k in range(n):
                    preSum[k] += matrix[j][k]
                    if sumMatrix <= 0 :
                        sumMatrix = preSum[k]
                        c1 = k  ##每次开始的时候，会记录下开始的列值、、、、或者确实让子矩阵和<0了， 就从k列开始
                    else:
                        sumMatrix += preSum[k]
                    if sumMatrix > maxSum:
                        maxSum = sumMatrix
                        ans = [i, c1, j, k]
        return ans
        # m = len(matrix)  # 行数
        # n = len(matrix[0])  # 列数
        # res = [0] * 4
        # max_val = matrix[0][0]  # 初始值
        # for i in range(m):
        #     nums = [0] * n  # 初始化行，转换为2维最大值求解
        #     for j in range(i, m):
        #         dp = 0  # dp初始化
        #         for k in range(n):
        #             nums[k] += matrix[j][k]  # 计算每1位，注意是累加，只有更新i，才刷新nums
        #             if dp <= 0:
        #                 dp = nums[k]
        #                 c1 = k  # 更新左边界
        #             else:
        #                 dp += nums[k]
        #             if dp > max_val:
        #                 max_val = dp
        #                 res = [i, c1, j, k]  # 更新res
        # return res