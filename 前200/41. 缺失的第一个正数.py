# -*- coding:utf-8 -*-
#
# 1. 去重 newNums = list(set(newNums))
# 2. 思路是 先去除小于0 的
#  把在范围内的值，放在指定位置。
# 依图面试的算法题。
#
# 第二次做的时候 忘记去重了

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def getNums(nums):

            newNums = [num for num in nums if num > 0]
            return newNums

        newNums = getNums(nums)
        newNums = list(set(newNums))

        # newNums = set(newNums)
        length = len(newNums)
        for i in range(length):
            num = newNums[i]
            if 0 < num <= length and newNums[num - 1] != num:
                newNums[i], newNums[num - 1] = newNums[num - 1], num
        i = 1
        for num in newNums:
            if num != i:
                return i
            i += 1
        return i
