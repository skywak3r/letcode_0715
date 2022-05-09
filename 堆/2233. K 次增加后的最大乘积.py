# -*- coding:utf-8 -*-
""""""
"""
方法一，
给最小值加1，再插入进去。二分插入。
超时

"""

"""
单一搜索加1，该移动到哪里。手动交换
超时

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        nums.sort()
        while  k > 0:
            k -= 1 
            r = 1
            nums[0] += 1
            while r <= len(nums) -1 and nums[0] > nums[r]:
                r += 1
            nums[0], nums[r-1] = nums[r-1], nums[0]
        tmp = 1
        for i in range(len(nums)):
            tmp = (tmp * nums[i])  % (10 ** 9 + 7)
        return tmp     
"""

"""
堆
动态极值

需要 学习 heapreplace


heapq.heappushpop(heap, item)
将 item 放入堆中，然后弹出并返回 heap 的最小元素。该组合操作比先调用 heappush() 再调用 heappop() 运行起来更有效率。
先push后pop

heapq.heapreplace(heap, item)
弹出并返回 heap 中最小的一项，同时推入新的 item。 堆的大小不变。 如果堆为空则引发 IndexError。
先pop 后push

"""
from heapq import heapify, heapreplace
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        heapify(nums)  # 直接调用 heapify nums 即可，不要另外赋值。
        while k:
            heapreplace(nums, nums[0] + 1)  #heapreplace 可以代替 pop 加push
            k -= 1
        ans = 1
        for num in nums: # 不用额外把nums pop出来。浪费时间
            ans = ans * num % MOD
        return ans
