# -*- coding:utf-8 -*-
"""
1.找参数和返回值
2.终止条件
3. for 循环 回溯

4. 减枝


"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path, ans = [], []

        def backtrack(n, k, start):
            if len(path) == k:
                ans.append(path.copy())
                return
            for i in range(start, n + 1):
                path.append(i)
                backtrack(n, k, i + 1)
                path.pop()

        backtrack(n, k, 1)
        return ans