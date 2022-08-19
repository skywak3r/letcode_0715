# -*- coding:utf-8 -*-
"""
2分法找。复杂度 NlogN  空间复杂度 O1
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def findNum(nums, remain):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] < remain:
                    left = mid + 1
                elif nums[mid] > remain:
                    right = mid
                else:
                    return mid
            return -1

        for i in range(len(nums)):
            remain = target - nums[i]
            index = findNum(nums, remain)
            if index != -1 :
                return [nums[i], nums[index]]


        return -1
"""

set 记住
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numSet = set(nums)
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in numSet:
                return [nums[i], remain]


        return -1
"""
双指针搜索

复杂度 on
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1

        while left < right:
            s = nums[left] + nums[right]
            if s < target:
                left += 1
            elif s > target:
                right -= 1
            else:
                return [nums[left], nums[right]]
        return []