# -*- coding:utf-8 -*-

"""
由于超出范围，所以不能使用max 函数。

贪心+ 循环取余。

前置：尽可能的三等分是最好的
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n < 4:
            return n -1
        if n == 4:
            return 4
        res = 1
        MOD = 10*9 +7
        while n < 4:
            res =  (res * 3) % MOD
            n -= 3
        return (res * n ) % MOD

"""

"""
快速幂


"""