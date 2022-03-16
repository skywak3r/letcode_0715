# -*- coding:utf-8 -*-
#只能出现一次
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) <= 0:
            return []
        res, path = [], []
        candidates.sort()
        self.backtrack(candidates, path, 0, len(candidates), target, res)
        return res

    def backtrack(self, candidates, path, begin, end, target, res):
        if target == 0:
            return res.append(path.copy())
        else:
            for i in range(begin, end):
                print(f"i:{i},target:{target}")
                if target - candidates[i] < 0:
                    break
                if i > begin and candidates[i] == candidates[i - 1]: continue###为了保证只出现一次

                path.append(candidates[i])
                # newCandidates = [candidate for candidate in candidates if candidate not in path]
                self.backtrack(candidates, path, i + 1, len(candidates), target - candidates[i], res) ###此处是i+1
                print(path)
                path.pop()
