# -*- coding:utf-8 -*-
"""
原因：对滑动窗口的存储处理有偏差。可以直接使用原数组的切片。

下面答案是 O(n^2)


"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        length = len(s)
        head, tail = 0, 0
        res = 1
        while tail < length:
            if s[tail] not in s[head:tail]:
                res = max(tail - head + 1, res)

            else:
                while s[tail] in s[head:tail]:
                    head += 1
            tail += 1

        return res
"""
使用hashmap，存储每个元素出现的最后位置。使用滑动窗口法。

使用tail去控制前进

通过head 和 tail的位置 实时计算当前的长度。

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        length = len(s)
        head = 0
        res = 0
        hashmap = {}
        for tail in range(length):
            if s[tail] in hashmap:
                head = max(head,hashmap[s[tail]])
            hashmap[s[tail]] = tail + 1
            res = max(res, tail - head + 1)
        return res



