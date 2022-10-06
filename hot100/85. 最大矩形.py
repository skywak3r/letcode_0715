# -*- coding:utf-8 -*-
"""
把问题转化为84题，

从左到右，看成一个高度列表，
从上刀下进行循环，不断送入不同的height，即可求出maxArea

https://leetcode.cn/problems/maximal-rectangle/solution/python3-qian-zhui-he-dan-diao-zhan-ji-su-vkpp/


前缀和思想（从上往下前缀

"""


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        def largestRectangleArea(heights: List[int]) -> int:

            leftMin = [-1] * len(heights)
            rightMin = [len(heights)] * len(heights)
            stack = []
            stack.append(0)
            for i in range(1, len(heights)):
                if heights[i] >= heights[stack[-1]]:
                    stack.append(i)
                else:
                    while stack and heights[stack[-1]] > heights[i]:
                        rightMin[stack[-1]] = i
                        stack.pop()

                    stack.append(i)
            stack = [len(heights) - 1]

            for i in range(len(heights) - 1, -1, -1):
                if heights[i] >= heights[stack[-1]]:
                    stack.append(i)
                else:
                    while stack and heights[stack[-1]] > heights[i]:
                        leftMin[stack[-1]] = i
                        stack.pop()
                    stack.append(i)
            # print(leftMin)
            # print(rightMin)
            ans = max([heights[i] * (rightMin[i] - leftMin[i] - 1) for i in range(len(heights))])
            return ans

        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])

        heights = [0] * n
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if (matrix[i][j] == "1"):
                    heights[j] += 1
                else:
                    heights[j] = 0
                    # print(heights)
                # print(largestRectangleArea(heights))
            maxArea = max(maxArea, largestRectangleArea(heights))

        return maxArea