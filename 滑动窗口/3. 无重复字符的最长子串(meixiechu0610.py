# -*- coding:utf-8 -*-

#滑动窗口我还不太会
"""
用外部控制左边界，for循环控制右边界。
如果进入窗口的重复了，一定是和左边界重复了，所以删除左边界在set中的值， 调整左边界的范围。


"""
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




