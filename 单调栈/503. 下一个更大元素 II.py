# -*- coding:utf-8 -*-
"""
转化为熟悉的问题：
将循环数组转换
"""
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)

        stack = [0]

        for i in range(2 * len(nums) -1):
            i = i % len(nums)
            if nums[i] <= nums[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) != 0 and nums[i] > nums[stack[-1]]:
                    ans[stack[-1]] = nums[i]
                    stack.pop()
                stack.append(i)
        return ans
