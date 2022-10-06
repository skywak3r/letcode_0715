# -*- coding:utf-8 -*-
"""
O（1时间获得最小值

设置一个辅助站，存放最小值。
每次push的时候，push进去 当前val和当前最小值的 最小值 存入辅助栈中

"""
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [float("inf")]
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()