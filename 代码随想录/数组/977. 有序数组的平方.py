# -*- coding:utf-8 -*-

"""
最大值要么最左边要么最右边



"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r = 0, len(nums)-1
        ans = [-1] * len(nums)
        cur = r
        while l<=r:
            lNum = nums[l]**2
            rNum = nums[r]**2
            if lNum>rNum:
                ans[cur] = lNum
                cur -= 1
                l += 1
            else:
                ans[cur] = rNum
                cur -= 1
                r -=1
        return ans
