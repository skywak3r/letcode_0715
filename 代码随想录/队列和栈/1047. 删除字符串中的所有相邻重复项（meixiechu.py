# -*- coding:utf-8 -*-
"""
"""
"""
用栈解决很好说。
"""
class Solution:
    def removeDuplicates(self, s: str) -> str:
        if len(s) == 1:
            return s
        ans = [s[0]]
        for i in range(1,len(s)):
            if ans and s[i] == ans[-1]:
                ans.pop()
            else:
                ans.append(s[i])
        return "".join(ans)
"""
双指针
"""