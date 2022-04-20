# -*- coding:utf-8 -*-
Counter的使用
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        counts = Counter(nums)
        return counts.most_common(1)[0][0]