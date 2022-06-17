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

"""
暴力法：
遍历每个点，找到左右最高的哪一个点，求出面积。
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height)):
            if i == 0 or i == len(height)-1: continue
            lHight = height[i-1]
            rHight = height[i+1]
            for j in range(i-1):
                if height[j] > lHight:
                    lHight = height[j]
            for k in range(i+2,len(height)):
                if height[k] > rHight:
                    rHight = height[k]
            res1 = min(lHight,rHight) - height[i]        
            if res1 > 0:
                res += res1
        return res
        

"""
"""
记忆化递归，把需要重复计算的左右最大值，先记录下来。
左最大值，从左到右
右最大值，从右到左，
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0 
        maxLeft = [height[0]] + [0] * (len(height)-1) 
        maxRight = [0] * (len(height)-1) + [height[-1]]
        for i in range(1,len(height)):
            maxLeft[i] = max(maxLeft[i-1],height[i])
        for j in range(len(height) - 2, -1, -1):
            maxRight[j] = max(maxRight[j+1], height[j])
        ans = sum([min(maxRight[i],maxLeft[i]) - height[i]  for i in range(len(height))])

        return ans 
"""


"""
双指针
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        leftMax = rightMax = 0
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if height[left] < height[right]:
                ans += leftMax - height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1
        
        return ans

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/trapping-rain-water/solution/jie-yu-shui-by-leetcode-solution-tuvc/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""