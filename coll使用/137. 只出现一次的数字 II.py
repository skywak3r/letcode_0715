# -*- coding:utf-8 -*-
import collections
class Solution:
    def singleNumber(self, nums: ) -> int:
        fre = collections.Counter(nums)
        ans = [num for num, occ in fre.items() if occ==1][0]
        return ans

"""
快速幂实现阶乘
1. 以二进制的视角去理解累乘。

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return x**n
        if n == 0:
            return 1
        if n < 0 :
            x,n = 1/x, -n
        ans = 1 
        while n > 0:
            if n&1:
                ans *= x
            x = x*x
            n >>= 1
        return ans 
            


"""