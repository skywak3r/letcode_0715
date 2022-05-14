# -*- coding:utf-8 -*-
""""""
"""
难点：1. 每次往前循环的是 对字符串的分割
2. 使用回溯法的思路
3. 我没有出详细的图


"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        length = len(s)
        ans = []
        path = []
        def judge(s):
            l,r = 0, len(s)-1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        def backtrack(index, path):
            if len("".join(path)) == length:
                ans.append(path.copy())
                return
            for i in range(index, length):
                tmp = s[index : i + 1]
                if judge(tmp):
                    path.append(tmp)
                    backtrack(i + 1, path)
                    path.pop()
        backtrack(0, path)
        return ans
