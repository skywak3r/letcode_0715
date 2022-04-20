# -*- coding:utf-8 -*-

"""
一步一步解决问题
分解成原子问题解决


"""

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        pre=  -1
        ans = [0] * len(s)
        for i in range(len(s)):
            if s[i] == c:
                pre = i

        for i in range(len(s)):
            if s[i] != c:
                ans[i] = abs(i-pre)
            else:
                ans[i] = 0
                pre = i
        for i in range(len(s)-1,-1,-1):
            if s[i] != c:
                ans[i] = min(abs(i-pre),ans[i])
            else:
                ans[i] = 0
                pre = i
        return ans


