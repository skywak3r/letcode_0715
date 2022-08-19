# -*- coding:utf-8 -*-
"""
用单调队列保持 一个有序的序列。在O1复杂度获得最大值



"""
class MaxQueue:
    def __init__(self):
        self.queue = []
        self.stack = []
    def max_value(self) -> int:
        if self.stack:
            return self.stack[0]
        else:
            return -1
    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while self.stack and self.stack[-1] < value:
            self.stack.pop()
        self.stack.append(value)
    def pop_front(self) -> int:
        if len(self.queue) == 0:
            return -1
        tmp = self.queue[0]
        if self.stack[0] == tmp:
            self.stack = self.stack[1:]
        self.queue = self.queue[1:]
        return tmp



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()