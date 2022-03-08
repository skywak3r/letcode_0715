# -*- coding:utf-8 -*-
"""

给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7


"""
#My sulotion
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []
        else:
            res = []
            for i in range(len(nums)+1-k):
                tmp = nums[i:i+k]
                res.append(max(tmp))
            return res

"""
优先队列（堆



"""