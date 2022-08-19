# -*- coding:utf-8 -*-
"""

思路： 从字符串结尾倒序， 加入res 数组里面。

"""

class Solution:
    def reverseWords(self, s: str) -> str:



        res = []
        s = s.strip()
        i, j = len(s)-1 ,len(s)-1
        while i >= 0:
            while s[i] != " " and i >= 0:  i -= 1
            res.append(s[i+1:j+1])
            while s[i] == " ":  i -= 1
            j = i
        return " ".join(res)
