# -*- coding:utf-8 -*-
"""
难点：
有两个只出现了1次的数字，并且空间复杂度 O1

方法：
1. 先获得a^b的值
2. 找到a^b这个值 某一位为1的时候，说明a和b在这一位是不同的。记作m
3， 按照m 将数组分成两个部分。  重新亦或。就变成了每个数组只有一个出现了一次的数字了
"""

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        aXorB = 0
        for num in nums:
            aXorB ^= num

#找 a和b在哪一位是不同的数字
        m = 1
        while (aXorB & m) == 0:
            m <<= 1



        x, y = 0, 0
        for num in nums:
            if m & num:
                x ^= num
            else:
                y ^= num
        return [x,y]
