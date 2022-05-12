# -*- coding:utf-8 -*-
""""""
"""
先把整体框架写出来，在慢慢去完善

单调队列的问题，没队列维持一个长度为k的窗口， 窗口向前移动时 保证队列是递减的。


"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque()
        ans = []
        for i, num in enumerate(nums):
            if queue and queue[0] == i -k :   ###窗口向前移动，先去调首元素
                queue.popleft()
            while queue and nums[queue[-1]] < num: ### 移除掉比当前值小的栈内元素
                queue.pop()
            queue.append(i) ###把当前值加入栈内
            if i >= k -  1: ###保证满足窗口k 后再加入ans中
                ans.append(nums[queue[0]])
        return ans
"""


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque()
        ans = []
        for i in range(len(nums)):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            left = i - k + 1
            if queue[0] < left:
                queue.popleft()
            if i >= k-1 :
                ans.append(nums[queue[0]])
        return ans 
        """
"""
堆的做法
先构造一个k的大顶堆，

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = [(-nums[i],i) for i in range(k)]  #构造一个大顶堆
        heapq.heapify(q)
        ans = [-q[0][0]]
        for i in range(k, len(nums)):  #遍历后面元素
            heapq.heappush(q, (-nums[i], i))    #先把元素push进来
            while q[0][1] <= i - k:  # 再去弹出需要弹出的元素，为了防止越界。  否则就在这个条件加上判断q是否为空
                heapq.heappop(q)
            ans.append(-q[0][0])
        return ans 
"""