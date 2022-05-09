# -*- coding:utf-8 -*-
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def change(num):
            src = []
            while num != 0:
                tmp = num % 10
                num //= 10
                src.append(tmp)
            tmp = 0
            for num in src:
                tmp += num ** 2
            return tmp

        src = change(n)
        while src != 1:
            if src in seen:
                return False
            seen.add(src)
            src = change(src)
        return True
