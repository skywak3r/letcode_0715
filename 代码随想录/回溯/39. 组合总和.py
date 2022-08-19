# -*- coding:utf-8 -*-
""""""
"""
这个题要求是组合数字， 所以在backtrack的时候要加上 start。
其次：因为可以重复，所以下一个start 是 i
如果是不可重复，start 是 i + 1
如果是排列数: 则不设置start

"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        ans = []
        def backtrack(candidates,start,path,target):
            if target == 0:
                ans.append(path.copy())
                return
            if target < 0 :
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(candidates, i,path, target - candidates[i])
                path.pop()
        backtrack(candidates,0,  path, target)
        return ans