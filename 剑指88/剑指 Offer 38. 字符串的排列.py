# -*- coding:utf-8 -*-
经典回溯发
不带重复的
class Solution:
    def permutation(self, s: str) -> List[str]:
        path, ans = [], []
        if len(s) ==1:
            return [s]

        used = [False] * len(s)
        def backtrack(s,start, end,path,used):
            if len(path) == len(s):
                ans.append(path.copy)
                return
            if start>end or used[start]  :
                return
            used[start] = True
            path += s[start]
            backtrack(s, start+1, end, path, used)
            used[start] = False
            path.remov

        backtrack(s,0,len(s)-1,path,used)
        return ans