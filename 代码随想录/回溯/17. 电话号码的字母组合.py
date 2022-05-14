# -*- coding:utf-8 -*-
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"qprs", "8":"tuv", "9":"wxyz"}
        path = []
        ans = []
        def backtrack(path,start):
            if len(path) == len(digits):
                ans.append("".join(path))
                return
            for i in range(start, len(digits)):
                for alpha in dic[digits[i]]:
                    path.append(alpha)
                    backtrack(path, i + 1)
                    path.pop()
        backtrack(path,0)
        return ans
