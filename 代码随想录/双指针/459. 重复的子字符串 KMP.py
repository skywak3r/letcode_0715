# -*- coding:utf-8 -*-
""""""
"""方法一：
暴力匹配法。找到相同的串，从头开始匹配。

条件： 一定要能被子串整除。 

差别： 其他都是末尾对fast操作。  我是开头操作的。 因为在break 和continue 会影响 fast的值。  且fast的值初始化时候，要比预先小1 。



"""
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s)==1:
            return False
        # fast, slow = 0, 0
        # flag = 0
        # while fast < len(s) - 1:
        #     fast += 1
        #     if s[fast] == s[slow]:
        #         element = s[slow:fast]
        #         # print(element)
        #         if len(s) % len(element) != 0 :
        #             continue
        #         count = 0
        #         for i in range(len(element),len(s)):
        #             if s[i] == element[i % len(element)]:
        #                 count += 1
        #         if count == len(s) - len(element):
        #             return True
        # return False

"""
方法2 ：
KMP 
找出最大相等的前后缀 next数组。
看最后一个字母的next数组跳到哪里。
如果跳的不是0 。 那么肯定有公共前缀。

并且  len(s) - 最后一个跳转的地方。 就是公共子串的长度。

如果可以被len(s)整除。 那么就是有子串组成的。
"""
        def getNext(s):
            length = len(s)
            next = [0] * length
            j = 0
            for i in range(1, length):
                while j > 0 and s[i] != s[j]:
                    j = next[j - 1]
                if s[j] == s[i]:
                    j += 1
                next[i] = j
            return next
        next = getNext(s)
        # print(next)
        if next[len(s) - 1] != 0 and len(s) % (len(s)-next[-1]) == 0:
            return True
        return False