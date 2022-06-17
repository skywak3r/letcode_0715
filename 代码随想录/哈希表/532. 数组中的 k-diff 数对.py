# -*- coding:utf-8 -*-
"""
o(N) 时间复杂度

额外判断特殊情况： k = 0 . k != 0

"""
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        count = Counter(nums)
        # print(count)
        for num in count.keys():
            remain = num - k
            if remain != num :
                if count[num - k]:
                    ans += 1
            else:
                if count[num] >= 2:
                    ans += 1
        return ans
