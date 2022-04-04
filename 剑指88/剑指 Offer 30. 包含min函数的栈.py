# -*- coding:utf-8 -*-
"""
使用辅助栈，
在每次push的时候，如果小于辅助站栈顶的值，就加入辅助站内
存储当前的最小值
"""
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st1 = []
        self.st2 = []

    def push(self, x: int) -> None:
        self.st1.append(x)
        if not self.st2 or self.st2[-1] >= x:
            self.st2.append(x)

    def pop(self) -> None:
        if self.st1.pop() == self.st2[-1]:
            self.st2.pop()

    def top(self) -> int:
        return self.st1[-1]

    def min(self) -> int:
        return self.st2[-1] if self.st2 else None
