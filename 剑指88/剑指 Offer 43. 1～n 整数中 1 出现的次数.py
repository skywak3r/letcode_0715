# -*- coding:utf-8 -*-


"""
划分为个位十位 百位。原子操作相加。

通过特殊例子，找出一般规律的不等式。而非空想


"""

class Solution:
    def countDigitOne(self, n: int) -> int:
        high, cur, low = n // 10, n % 10, 0
        src = 0
        digit = 1
        while high != 0 and cur != 0:
            if cur == 0:
                src += high * digit
            elif cur == 1:
                src += high * digit + low + 1
            else:
                src += (high + 1) * digit
            low += cur * digit
            cur = high % 10
            high //= 10

            digit *= 10
        return src
