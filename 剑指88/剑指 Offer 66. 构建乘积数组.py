# -*- coding:utf-8 -*-
"""
考虑特殊情况，在开头的地方

难点是不用除法。下面方法不行。


"""
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        res = 1
        count = a.count(0)
        if len(a) == 0:
            return []
        if count > 1:
            return [0] * len(a)
        for i in range(len(a)):
            res *= a[i]
        b = []
        for i in range(len(a)):
            if a[i] != 0:
                b.append(res//a[i])
            else:
                tmp = 1
                for j in range(len(a)):
                    if j != i:
                        tmp *= a[j]
                print(tmp)
                b.append(tmp)
        return b
"""
正确解法：
用一个前缀乘积和后缀乘积。


"""