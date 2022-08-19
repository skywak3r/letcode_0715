# -*- coding:utf-8 -*-
"""
https://leetcode.cn/problems/next-permutation/solution/xia-yi-ge-pai-lie-suan-fa-xiang-jie-si-lu-tui-dao-/

1. 从后往前找第一个相邻的升序对， ij
2. 在j，end 中招一个比nums[i 大的值， 交换他俩
3. 把j,end 的数字 变成升序



"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        i, j, k = len(nums) - 2, len(nums) - 1, len(nums) - 1
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1

        if i >= 0:
            while nums[i] >= nums[k]:
                k -= 1
            nums[i], nums[k] = nums[k], nums[i]

        l, r = j, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1



