# -*- coding:utf-8 -*-

Counter的∩操作。

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        tmp = collections.Counter(words[0])
        for i in range(1,len(words)):
            tmp = tmp & Counter(words[i])
        ans = []
        for alpha, count in tmp.items():
            while count > 0:
                ans.append(alpha)
                count -= 1
        return ans