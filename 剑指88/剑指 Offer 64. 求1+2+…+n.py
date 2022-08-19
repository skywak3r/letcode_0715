# -*- coding:utf-8 -*-
"""
不用加减乘除和判断循环语句。

递归方法 + 与运算方法

"""
class Solution:
    def __init__(self):
        self.res = 0
    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n-1)
        self.res += n

        return self.res