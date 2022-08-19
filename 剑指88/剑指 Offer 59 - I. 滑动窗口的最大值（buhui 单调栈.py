# -*- coding:utf-8 -*-
"""
重点：  单调栈和找到循环的变量。


我循环的变量是窗口的尾部
https://leetcode.cn/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/solution/hua-dong-chuang-kou-de-zui-da-zhi-by-lee-ymyo/

"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        stack = collections.deque()
        if len(nums) == 0:
            return []
        for i in range(k): # 先造一个窗口，省的循环的时候额外判断。
            while stack and nums[i] > nums[stack[-1]]:
                stack.pop()
            stack.append(i)
        #记住单调栈里面存的都是index
        res.append(nums[stack[0]])


        for i in range(k, len(nums)):#此处控制的是尾部

            while stack and nums[i] > nums[stack[-1]]:
                stack.pop()
            stack.append(i)
            while stack[0] <= i - k:  # 控制头部的index是不是在窗口内，不在就pop掉
                stack.popleft()
            res.append(nums[stack[0]])
        return res