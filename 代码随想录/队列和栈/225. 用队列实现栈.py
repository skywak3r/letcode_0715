# -*- coding:utf-8 -*-

""""""

"""
用一个deque实现 stack
"""
class MyStack:

    def __init__(self):
        self.queue1 = collections.deque()
    def push(self, x: int) -> None:
        self.queue1.append(x)
    def pop(self) -> int:
        length = len(self.queue1)
        if self.empty() :
            return None
        for i in range(length - 1):
            self.queue1.append(self.queue1.popleft())
        return self.queue1.popleft()
    def top(self) -> int:
        if self.empty():
            return None
        else:
            ans = self.pop()
            self.push(ans)
            return ans
    def empty(self) -> bool:
        if len(self.queue1):
            return False
        else:
            return True

