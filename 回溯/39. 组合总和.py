# -*- coding:utf-8 -*-
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        length = len(candidates)
        if length <= 0:
            return []
        candidates.sort()
        res = []
        path = []
        self.backtrack(candidates, path, target, 0, len(candidates), res)
        return res

    def backtrack(self, candidates, path, target, begin, size, res):
        if target == 0:
            res.append(path.copy())
        else:
            for i in range(begin, size):
                left_num = target - candidates[i]
                if left_num < 0: break
                path.append(candidates[i])
                self.backtrack(candidates, path, left_num, i, size, res)
                path.pop()



