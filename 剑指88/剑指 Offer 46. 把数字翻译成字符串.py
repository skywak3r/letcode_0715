# -*- coding:utf-8 -*-
"""
看能把问题分解成子问题。
以s[:i]结尾的翻译的个数，和最后一个字母和倒数第二个字母有关。
如果这两个字母可以组成一个，那就是一种情况
如果组成的数字大于25，那就是另一种情况



"""

class Solution:
    def translateNum(self, num: int) -> int:
        strNum = list(str(num))
        length = len(strNum)
        if length < 2:
            return length

        dp = [0] * (length + 1)
        dp[0] = 1
        dp[1] = 1
        # print(strNum)
        for i in range(2, length + 1):
            if 10 <= int(strNum[i - 2] + strNum[i - 1]) < 26:
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        # print(dp)
        return dp[-1]