# -*- coding:utf-8 -*-
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        length = len(digits)
        if length == 0:
            return []
        dic = {"0": "", "1": "", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "qprs", "8": "tuv",
               "9": "wxyz"}
        path, ans = "", []

        def backtrack(start, innerIndex):
            nonlocal path
            if len(path) == length:
                ans.append(path[:])
                return
            for i in range(start, length):
                for j in range(len(dic[digits[i]])):
                    path += dic[digits[i]][j]
                    # path.append(dic[digits[i]][j])
                    backtrack(i + 1, j + 1)
                    path = path[:-1]

        backtrack(0, 0)
        return ans