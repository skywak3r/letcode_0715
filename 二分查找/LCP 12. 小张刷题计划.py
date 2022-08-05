# -*- coding:utf-8 -*-
"""

题目关键： 连续，非负。


这样方法 比较繁琐。
下方方法更好

"""
class Solution:
    def minTime(self, time: List[int], m: int) -> int:
        left, right = 0, sum(time)
        def split(nums, mid, m ): #返回每天使用mid的时间，最少可以分割几天
            #比较难受的是如何判断是否已经求助了，这里直接使用每次比最大值 小的那个值去加
            curMax = nums[0]
            curSum = 0
            count = 1
            # is_help = [False] * (len(nums))
            for i in range(1, len(nums)):
                # tmp = min(nums[i], curMax) + curSum
                # curMax = max(curMax, nums[i])

                if curSum + min(curMax , nums[i]) <= mid:
                    curSum = curSum + min(curMax, nums[i])
                    curMax = max(curMax, nums[i])
                else:
                    count += 1
                    curMax = nums[i]
                    curSum = 0
            return count
        while left < right:
            mid = left + (right - left) // 2
            count = split(time, mid, m )
            if count > m :
                left = mid + 1
            else:
                right = mid
        return left

"""

每次不管是啥我都加，
加了之后，再减去最大值。意思是求助了。

如果减了最大值之后还是超了，那么久下一天。
下一天的初始化： 当前的nums[i]

"""
class Solution:
    def minTime(self, time: List[int], m: int) -> int:
        left, right = 0, sum(time)
        def split(nums, mid, m ):
            count = 1
            curSum, curMax = 0, 0
            for i in range(len(nums)):
                curMax = max(curMax, nums[i])
                curSum += nums[i]
                if curSum - curMax > mid:
                    count += 1
                    curSum = nums[i]
                    curMax = nums[i]
            return count


        while left < right:
            mid = left + (right - left) // 2
            count = split(time, mid, m )
            if count > m :
                left = mid + 1
            else:
                right = mid
        return left