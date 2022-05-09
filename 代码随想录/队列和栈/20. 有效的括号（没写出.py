# -*- coding:utf-8 -*-
"""
先分析好情况，再去写代码。不是运气游戏
把问题考虑全面


"""

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)% 2 != 0:
            return False
        dic = {"(":")", "{":"}", "[":"]"}
        queue = []
        for item in s:
            if item in dic.keys():
                queue.append(dic[item])
            elif queue and queue[-1] == item:
                queue.pop()
                # return False
            else:
                # queue.pop()
                return False
        return True if len(queue) == 0 else False
