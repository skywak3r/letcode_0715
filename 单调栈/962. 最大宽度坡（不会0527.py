# -*- coding:utf-8 -*-

""""""
"""
为了找到某个数的最长的递增数的位置。

首先先从开头记录一个单调递减的序列

然后在再从末尾到开头 依次和栈内的 比较 。记录最长位置。

最小的坡的 左边  肯定在这个递减区间里面

"""
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = [0]
        ans = -1
        for i in range(1,len(nums)):
            if not stack or nums[stack[-1]] >= nums[i]:
                stack.append(i)
        # print(stack)
        for i in range(len(nums)-1, -1,-1):
            while stack and nums[stack[-1]] <= nums[i]:
                pos = stack.pop()
                ans = max(ans, i - pos)
        return ans