# -*- coding:utf-8 -*-
"""
归并算法

分解完成之后，再逐步合并有序数列。



"""

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0
        if len(nums) == 0:
            return 0

        def merge(nums, left, mid, right):
            l_pos, r_pos = left, mid + 1
            tmp = []
            while l_pos <= mid and r_pos <= right:
                if nums[l_pos] <= nums[r_pos]:
                    tmp.append(nums[l_pos])
                    l_pos += 1
                else:
                    tmp.append(nums[r_pos])
                    self.count += mid - l_pos + 1  ### 如果逆序了，就是从左半部分结尾到 l_pos 处的数量
                    r_pos += 1
            while l_pos <= mid:
                tmp.append(nums[l_pos])
                l_pos += 1
            while r_pos <= right:
                tmp.append(nums[r_pos])
                r_pos += 1
            for i in range(len(tmp)):
                nums[left + i] = tmp[i]

        def mergeSort(nums, left, right):
            if left >= right:
                return
            mid = left + (right - left) // 2
            mergeSort(nums, left, mid)
            mergeSort(nums, mid + 1, right)
            merge(nums, left, mid, right)

        mergeSort(nums, 0, len(nums) - 1)
        return self.count
