# -*- coding:utf-8 -*-
"""
分段的有序数列，还是用二分法。
首先确定二分搜索的范围。   分开两个区间，总有一个有序的，去有序的那一段搜索


"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r)>>1
            if nums[mid] == target:
                return mid
            if nums[l] < nums[mid]: #确定单调区间
                if nums[l] <= target < nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums)-1]:
                    l = mid + 1
                else:
                    r = mid
        return -1