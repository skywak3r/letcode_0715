# -*- coding:utf-8 -*-
"""
二分很好的解析
https://leetcode.cn/problems/binary-search/solution/er-fen-cha-zhao-xiang-jie-by-labuladong/




使用两次二分查找，分别找出 左右边界。

我所掌握的二分 都是 左闭右开的，尽可能的使得mid 往左边切近，

这里的第二次二分就要，尽可能的右边贴近


搜索左边界得到的结果是：   比target 小的有几个数字

二分不用要else： 所有情况都要在elif中找到


"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)
        L, R = -1, -1

        if not nums:
            return [-1,-1]
        while l < r:
            mid = (l + r) >>1
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid
            else:
                r = mid

        # 返回
        L = l
        # print(l)
        if L == len(nums) or nums[L] != target:  # 看找到的是否在数组中
            return [-1,-1]
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] == target:
                l = mid + 1  # 不断所有左边界
            elif nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        R = l - 1     # 注意： 比target小的有l个数字，那么 l-1就是我的target
        return [L,R]
