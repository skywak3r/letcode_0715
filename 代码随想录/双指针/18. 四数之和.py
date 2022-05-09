# -*- coding:utf-8 -*-
"""
三数之和的基础上增加一个for循环

"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:  #去重
                continue
            for j in range(i+1, len(nums)):
                if j > i+ 1 and nums[j] == nums[j-1]:  #去重
                    continue
                l, r = j+1, len(nums)-1
                while l < r :
                    if nums[i] + nums[j] + nums[l] + nums[r] > target:
                        r-=1
                    elif nums[i] + nums[j] + nums[l] + nums[r] < target:
                        l += 1
                    else:
                        ans.append([nums[i],nums[j],nums[l],nums[r]])
                        while l < r and nums[l] == nums[l+1]:  #去重
                            l+= 1
                        while l < r and nums[r] == nums[r-1]:
                            r-= 1
                        l += 1
                        r -= 1
        return ans