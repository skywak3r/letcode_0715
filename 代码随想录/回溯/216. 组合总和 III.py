# -*- coding:utf-8 -*-
""""""
"""
backtrack 的参数还写错了

写成了backtrack(path, target - i, index + 1) 
这样就没有一步一步往前缩小搜索范围了。

而且没审清楚题。 正整数0-9

"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []
        def backtrack(path, target, index):
            if len(path) == k and target == 0:
                ans.append(path.copy())
                return
            for i in range(index, 10):
                path.append(i)
                backtrack(path, target - i, i + 1)
                path.pop()
        backtrack(path, n, 1)
        return ans