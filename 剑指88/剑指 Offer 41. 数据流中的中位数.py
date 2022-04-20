# -*- coding:utf-8 -*-

用堆维护一个大数组和小数组。




class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.big = []
        self.small = []
    def addNum(self, num: int) -> None:
        if len(self.big) != len(self.small):
            heapq.heappush(self.big, num)
            heapq.heappush(self.small,-heapq.heappop(self.big))
        else:
            heapq.heappush(self.small, -num)
            heapq.heappush(self.big, -heapq.heappop(self.small))
        # print(self.big)
        # print(self.small)

    def findMedian(self) -> float:
        return self.big[0] if len(self.big) != len(self.small) else (self.big[0]-self.small[0])/2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()