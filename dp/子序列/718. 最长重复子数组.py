# -*- coding:utf-8 -*-
"""
有两个数组： 所以需要二维数组，要构造一个无后效性的dp。

dp[i][j] 表示前A的前i个 和B的前j个的相同的数目

"""

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        length1 = len(nums1)
        length2 = len(nums2)

        dp = [[0] * (length2+1) for _ in range(length1+1)]

        for i in range(1,length1+1):
            for j in range(1,length2+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
        result = max([max(row) for row in dp])
        # print(dp)
        return result
"""
滑动窗口：
maxlength 函数用于比较当前对其情况下的结果。
下方两个for循环是用于遍历出所有的对其情况。
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def maxLength(addA, addB, length):
            ret, k = 0, 0
            for i in range(length):
                if nums1[addA + i] == nums2[addB + i]:
                    k += 1
                    ret = max(ret, k)
                else:
                    k = 0 
            return ret 
        n, m = len(nums1), len(nums2)
        ret = 0 

        for i in range(n):
            length = min(m, n -i)
            ret = max(ret, maxLength(i, 0, length))
        for i in range(m):
            length = min(n, m-i)
            ret = max(ret, maxLength(0, i, length))
        return ret 
        
"""

