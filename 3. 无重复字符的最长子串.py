# -*- coding:utf-8 -*-

#滑动窗口我还不太会

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        begin = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for end in range(n):
            cur_len += 1
            while s[end] in lookup:
                lookup.remove(s[begin])
                begin += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[end])
        return max_len




