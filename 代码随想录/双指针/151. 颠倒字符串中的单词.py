# -*- coding:utf-8 -*-
"""
字符串处理
直接倒序添加原句的单词即可， 看剑指88

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split(" ")
        # print(words)
        res = [word for word in words if word != ""]
        return " ".join(res[::-1])

"""

"""
双指针



class Solution:
    def reverseWords(self, s: str) -> str:
        def removeSpace(s):
            l = 0 
            r = len(s) -1 
            while l <= r and s[l] == " ":
                l += 1
            while l <= r and s[r] == " ":
                r -= 1
            tmp = []
            while l <= r:
                if s[l] != " ":
                    tmp.append(s[l])
                else:
                    if s[l-1] != " ":
                        tmp.append(s[l])
                l += 1
            return "".join(tmp)
        newS = removeSpace(s)
        def reverseStr(s):
            l, r = 0, len(s)-1
            tmp = list(s)
            while l <= r:
                tmp[l],tmp[r] =tmp[r], tmp[l]
                l += 1
                r -= 1
            return "".join(tmp) 
        def reverseWord(s):
            l, r = 0, 0
            tmp = list(s)
            while r < len(s):
                if tmp[r] == " ":
                    cur = r - 1
                    while l <= cur:
                        tmp[l], tmp[cur] = tmp[cur], tmp[l]
                        l += 1
                        cur -= 1
                    l = r + 1
                r += 1
            # print(tmp)
            r = len(s) -1 
            while l <= r :
                tmp[l], tmp[r] = tmp[r], tmp[l]
                r -= 1
                l += 1
            return "".join(tmp)

        newS1 = reverseStr(newS)
        # print(newS1)
        newS2 = reverseWord(newS1)
        # print(newS2)
        return newS2

"""