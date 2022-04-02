# -*- coding:utf-8 -*-
"""
求出二进制序列，统计1的个数即可
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        def bit(n):
            src = []
            while n > 0:
                tmp = n & 1
                n = n >> 1
                src.append(tmp)
            return src
        return bit(n).count(1)