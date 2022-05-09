# -*- coding:utf-8 -*-
"""
没做出来。
首先定义一个翻转函数。
至于变换范围的事情。是另一回事。
使用for (start, stop, step) 控制范围。


"""
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse(s):
            length = len(s)
            l, r = 0, len(s) - 1
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            return s
        s = list(s)
        for cur in range(0, len(s) - 1, 2 * k):
            s[cur : cur + k ] = reverse(s[cur : cur + k])
        return "".join(s)
