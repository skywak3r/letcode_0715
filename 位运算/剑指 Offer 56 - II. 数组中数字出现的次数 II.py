# -*- coding:utf-8 -*-
"""
统计每一位 bit出现的次数，如果是3的倍数 那没事
如果不是 ，那就亦或 res。32位亦或完成  就是答案

"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            bits = 2 ** i
            count = 0
            for num in nums:
                if num & bits != 0:
                    count += 1
                # print(num ,bits, count)
            if count % 3 != 0:
                res = bits ^ res
        return res

