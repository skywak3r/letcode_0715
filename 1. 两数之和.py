# -*- coding:utf-8 -*-
"""
暴力解决
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

#哈希表
hash.get
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for idx,num in enumerate(nums):
            hashMap[num] = idx
        for j, num in enumerate(nums):
            tmp = target - num
            i = hashMap.get(tmp)
            if i is not None and i !=j:
                return [i,j]



"""