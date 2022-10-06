# -*- coding:utf-8 -*-
"""
手写快速排序。
但是此题只有3个数字，  可以直接使用两次 交换就可以实现有序。



"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def partition(nums, left, right):
            baseNum = nums[left]
            l, r = left, right
            while l < r:
                while l < r and nums[r] >= baseNum:
                    r -= 1
                nums[l] = nums[r]
                while l < r and nums[l] <= baseNum:
                    l += 1
                nums[r] = nums[l]
            nums[l] = baseNum
            return l

        def quicksort(nums, left, right):
            if left < right:
                index = partition(nums, left, right)
                quicksort(nums, left, index)
                quicksort(nums, index + 1, right)

        quicksort(nums, 0, len(nums) - 1)

"""
直接两次循环遍历


"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p0, p1 = 0,0
        for i in range(n):
            if nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                if p0 < p1:# 把头部的1 交换到0的后面
                    nums[i], nums[p1] = nums[p1], nums[i]
                p0 += 1
                p1+= 1
