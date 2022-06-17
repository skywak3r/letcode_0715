# -*- coding:utf-8 -*-
"""

dp
"""
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 0
        if len(nums) < 2:
            return len(nums)

        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] = max(dp[i], dp[i - 1] + 1)
        return max(dp)

"""
迭代法

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 0 
        count = 1
        if len(nums) < 2:
            return len(nums)
        for i in range(len(nums) - 1 ):
            if nums[i+1] > nums[i]:
                count += 1 
            else:
                count = 1
            ans = max(ans, count)
        return ans 
        
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        length = len(nums)
        l,r = 0,1
        ans = 1
        while r < length:
            tmp = 1
            while r < length and nums[r] > nums[l]:
                tmp += 1 
                r += 1
                l += 1
                ans = max(tmp, ans)
            l += 1
            r += 1
        return ans 
            
"""