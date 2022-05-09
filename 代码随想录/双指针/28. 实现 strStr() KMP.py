# -*- coding:utf-8 -*-

""""""

"""
主逻辑：遍历主串，如果相等，模式串的index 加一。如果不等，按照next 往前回退。 
知道j == 模式串的长度
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def getNext(src):
            #初始化
            next = [0] * len(src)
            j = 0   # 代表前缀的末尾
            for i in range(1, len(next)):  # i 代表后缀的末尾
                # 前缀末尾和后缀末尾不相同 ： 前缀末尾往前走
                while (j>0 and src[j] != src[i]):
                    j = next[j - 1]
                # 前缀末尾等于后缀末尾：
                if src[i] == src[j]:
                    j += 1
                next[i] = j
            return next
        next = getNext(needle)
        j = 0
        for i in range(len(haystack)):
            while (j > 0 )and haystack[i] != needle[j]:
                j = next[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - len(needle) + 1
        return -1