# -*- coding:utf-8 -*-
"""
dp
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = int((dp[i-1] + dp[i-2])%(1e9+7))

        return dp[-1]

"""

"""
3变量
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n 
        prepre,pre,cur = 0,1,1
        i = 1
        while i<n:

            prepre = int(pre % (1e9+7))
            pre = int(cur % (1e9+7))
            cur = int((cur + prepre)%(1e9+7))
            i += 1 
        return pre
"""
"""
快速幂


class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n 
        MOD = 10**9 +7 
        tmp = [[1,1],[1,0]]
        tmp1 = [1,0]


        def multi(num1, num2):
            src = [[0,0],[0,0]]
            for i in range(2):
                for j in range(2):
                    src[i][j] = (num1[i][0] * num2[0][j] + num1[i][1] * num2[1][j]) % MOD
            return src
        def multi2(num1):
            src = [[0],[0]]
            for i in range(2):
                src[i][0] = num1[i][0] * 1 + num1[i][1] * 0
            return src

        def multiPow(n):
            if n == 1:
                return tmp
            if n == 2:
                return multi(tmp, tmp)
            b = n % 2
            if b:
                return multi(multi(multiPow(n >> 1), multiPow(n>>1)),tmp)
            else:
                return multi(multiPow(n >> 1),multiPow(n>>1))
        return multi2(multiPow(n))[1][0]
"""