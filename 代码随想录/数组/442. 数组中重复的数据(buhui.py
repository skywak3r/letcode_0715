# -*- coding:utf-8 -*-
""""""
"""
在交换数组的时候，要注意顺序
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                # nums[i], nums[nums[i] -1 ] = nums[nums[i] - 1], nums[i]
                
在第二行代码，在交换第二个的时候，nums【i 已经改变。
"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # for i in range(len(nums)):
        #     while nums[i] != nums[nums[i] - 1]:
        #         nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        # return [num for i, num in enumerate(nums) if num - 1 != i]

        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                # nums[i], nums[nums[i] -1 ] = nums[nums[i] - 1], nums[i]
        return [num for i, num in enumerate(nums) if num - 1 != i]
