# -*- coding:utf-8 -*-
"""
求最长公共子列的的应用题。 将问题抽象成  相对顺序不变的 最长子序列是。

"""
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        length1 = len(nums1)
        length2 = len(nums2)

        if length1 == 0 or length2 == 0:
            return 0

        dp = [[0] * (length2 + 1) for _ in range(length1 + 1)]

        for i in range(1, length1 + 1):
            for j in range(1, length2 + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        result = max([max(row) for row in dp])
        # print(dp)
        return result

