# -*- coding:utf-8 -*-
"""
平安产险 面试题

目标： 对于arr1中的数字num

如果 num 与 arr2中的所有数字之间的距离 大于d， 那么ans+= 1

思路：
对arr2排序。 在arr2中二分查找出 num的位置。 （距离num最近的）

"""
import bisect

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        ans = 0
        for num in arr1:
            index = bisect.bisect_left(arr2, num)
            # print(index)
            if 0 < index < len(arr2) and abs(num - arr2[index]) > d and abs(num - arr2[index - 1] > d):
                ans += 1

            if index == 0 and abs(num - arr2[0]) > d:
                ans += 1
            if index == len(arr2) and abs(num - arr2[-1]) > d:
                ans += 1
        return ans

