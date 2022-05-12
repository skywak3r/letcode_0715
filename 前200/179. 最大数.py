# -*- coding:utf-8 -*-
""""""
"""
sroted 的使用
两个数构成最大值-》直接修改成字典序
functools.com_to_key   返回值是1,0，-1   1不交换，-1交换，0不动
"""

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = list(map(str, nums))
        def cmp(x,y):
            if x + y > y + x:
                return -1
            elif x + y < y + x :
                return 1
            else:
                return 0
        res = sorted(nums_str, key = functools.cmp_to_key(cmp))
        # print(res)
        if res[0] == "0":
            res = "0"

        return "".join(res)