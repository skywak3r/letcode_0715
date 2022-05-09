# -*- coding:utf-8 -*-

"""
要找到左右两边小于当前的值，
构造两个列表

重点：：对于边界值的处理。如果最小值没有比他小的。那么他的就是边界


"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        leftMin = [-1] * len(heights)
        rightMin = [len(heights)] * len(heights)
        stack = []
        stack.append(0)
        for i in range(1,len(heights)):
            if heights[i] >= heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and heights[i] < heights[stack[-1]]:
                    rightMin[stack[-1]] = i
                    stack.pop()
                stack.append(i)
        stack = []
        stack.append(len(heights)-1)
        for j in range(len(heights)-2,-1,-1):
            if heights[j] >= heights[stack[-1]]:
                stack.append(j)
            else:
                while stack and heights[j] < heights[stack[-1]]:
                    leftMin[stack[-1]] = j
                    stack.pop()
                stack.append(j)
        ans = max((rightMin[i] - leftMin[i] -1) * heights[i] for i in range(len(heights))) if len(heights)>0 else 0
        return ans if ans >= 0 else 0


