# -*- coding:utf-8 -*-
import bisect
"""
bisect.insort 之后就是有序的列表
lo <= pre(j)-pre(i-1)<=upper
如果求出前缀和之后，再一一比较，复杂度是n^2

所以使用二分查找。
使用preWindows 控制当前的有序sum前缀和



"""
class Solution:
    def countRangeSum(self, A: List[int], lower: int, upper: int) -> int:
        sumList = [0]

        for i in range(len(A)):
            sumList.append(sumList[-1] +A[i])
        src = 0
        preWindows = []
        for i,p in enumerate(sumList):
            L = bisect.bisect_left(preWindows, p-upper)
            # Lr = bisect.bisect_right(preWindows, p-upper)
            print(f"p:{p}")
            print(f"L_left:{L}")
            # print(f"L_right:{Lr}")
            R = bisect.bisect_right(preWindows, p-lower)
            src += R-L
            bisect.insort(preWindows, p)
        return src