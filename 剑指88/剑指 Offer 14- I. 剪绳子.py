# -*- coding:utf-8 -*-:
"""
尽可能分成三等分
我写的代码2等分了，只能过一部分的案例

使用大顶堆，每次将大顶堆的最大值一分为2  看是否乘积增加，

class Solution:
    def cuttingRope(self, n: int) -> int:
        factor = []
        def multiMax(nums):
            ans = 1
            for i in nums:
                ans *= -i
            return ans
        heapq.heappush(factor,-n)
        # heapq.heappush(factor,-4)
        src = 1
        # print(multiMax([3,4,5]))
        def split(nums):
            maxFac = -1 * heapq.heappop(nums)
            src1 = maxFac // 2
            src2 = maxFac - src1
            heapq.heappush(nums,-src1)
            heapq.heappush(nums,-src2)
            return nums
        # heapq.heappush(factor, -9)
        # print(split(factor))

        # test = [-3,-2,-2]
        # test1 = split(test)
        # print(f"test:{test}")
        # print(multiMax(test))
        if n <4:
            return n-1
        while True:
            factor = split(factor)
            tmp = multiMax(factor)
            if tmp > src:
                src = tmp
                continue
            break
            # print(src)
            # print(factor)
        # print(factor)
        return src




"""

"""
dp

绳子切割问题： 前面长度为j   后面长度i-j
前面的部分是不剪的部分，
后面可以剪  j dp[i-j]
不剪： j * (i-j)
当前的 dp
三者取最大

class Solution:
    def cuttingRope(self, n: int) -> int:
        if n < 4:
            return n -1
        dp = [0] * (n+1)
        dp[2] = 1

        for i in range(4,n+1):
            for j in range(2,i):
                dp[i] = max([dp[i-j]*j,(i-j)*j,dp[i]])
        return dp[-1]

"""