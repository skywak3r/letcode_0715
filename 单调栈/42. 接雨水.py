# -*- coding:utf-8 -*-
"""
https://github.com/skywak3r/leetcode-master/blob/master/problems/0042.%E6%8E%A5%E9%9B%A8%E6%B0%B4.md

单调栈的方法：
横着看 求出雨水面积

"""
class Solution:
    def trap(self, height: List[int]) -> int:
        nextGreat = [-1] * len(height)
        stack = [0]
        ans = 0

        for i in range(len(height)):
            if height[i] < height[stack[-1]]:
                stack.append(i)
            elif height[i] == height[stack[-1]]:
                stack.pop()
                stack.append(i)

            else:
                while len(stack) != 0 and height[i] > height[stack[-1]]:
                    midHeight = height[stack[-1]]
                    stack.pop()
                    if stack:
                        rightHeigt = height[i]
                        leftHeight = height[stack[-1]]  # pop后就是左边的高度
                        h = min(rightHeigt,leftHeight) -midHeight
                        w = i - stack[-1] - 1
                        ans += h * w
                stack.append(i)
        return ans
