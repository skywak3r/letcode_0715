# -*- coding:utf-8 -*-
"""
"""
"""
此题要求：数组有重复，但是返回的ans 不能有重复的组合。

去重要用used数组

上方的要求： 画出树状图，意思是 同一颗树上，可以有重复，但是用一层不能重复使用。

used[i - 1] == true，说明同一树枝candidates[i - 1]使用过
used[i - 1] == false，说明同一树层candidates[i - 1]使用过
这块去重的逻辑很抽象，网上搜的题解基本没有能讲清楚的，如果大家之前思考过这个问题或者刷过这道题目，看到这里一定会感觉通透了很多！


如果直接求出所有的组合再去set去重会超时。

"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        ans = []
        candidates.sort()
        seen = set()
        def backtrack(candidates,start,path,target,used):
            if target == 0:
                ans.append(path.copy())
                return
            if target < 0 :
                return
            for i in range(start, len(candidates)):
                if i > 0 and candidates[i-1] == candidates[i] and not used[i-1]:
                    continue
                path.append(candidates[i])
                used[i] = True
                backtrack(candidates, i + 1,path, target - candidates[i],used)
                used[i] = False
                path.pop()
        used = [False] * len(candidates)
        backtrack(candidates,0, path, target,used)
        return ans