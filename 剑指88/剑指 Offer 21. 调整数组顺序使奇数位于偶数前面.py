# -*- coding:utf-8 -*-
"""
双端列表
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        ans = collections.deque()
        for num in nums:
            if num & 1 == 0:
                ans.append(num)
            else:
                ans.appendleft(num)
        return list(ans)
"""
"""
双指针
i从前向后找偶数
j从后向前找奇数

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums)-1

        while j>i:
            while j>i and nums[i] & 1 == 1: 
                i += 1
            while j>i and nums[j] & 1 == 0:
                 j -=1
            nums[i], nums[j] = nums[j], nums[i]
        return nums

"""