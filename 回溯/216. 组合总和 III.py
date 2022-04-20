# -*- coding:utf-8 -*-

"""
回溯三部曲
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        path, ans = [], []
        def backtrack(curSum, k, start):
            if len(path) == k:
                if n == curSum:
                    ans.append(path.copy())
                return
            for i in range(start,10):
                path.append(i)

                backtrack(curSum+i, k, i+1)
                path.pop()
        backtrack(0, k, 1)
        return ans