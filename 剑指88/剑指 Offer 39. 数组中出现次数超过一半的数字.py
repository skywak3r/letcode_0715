# -*- coding:utf-8 -*-
"""Counter的使用

时间复杂度 O(n) 空间复杂度 ON

难点：摩尔投票发：  O(1)空间复杂度

"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        counts = Counter(nums)
        return counts.most_common(1)[0][0]

"""
O1空间复杂度。

结论： 当数组减少一半， 众数还是众数，不会变得。

方法： 摩尔投票法： 核心理念为 票数正负抵消 

若记 众数 的票数为 +1，非众数 的票数为 -1 ，则一定有所有数字的 票数和 > 0>0 。


算法流程:
初始化： 票数统计 votes = 0 ， 众数 x；
循环： 遍历数组 nums 中的每个数字 num ；
当 票数 votes 等于 0 ，则假设当前数字 num 是众数；
当 num = x 时，票数 votes 自增 1 ；当 num != x 时，票数 votes 自减 1 ；
返回值： 返回 x 即可；




"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        for num in nums:
            if votes == 0:
                x = num
            votes += 1 if num == x else -1

        return x