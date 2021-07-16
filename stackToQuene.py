# -*- coding:utf-8 -*-

class CQueue:
"""
剑指 Offer 09. 用两个栈实现队列
耗时太长了
"""
    def __init__(self):
        self.res = []
        self.s1 = []

    def appendTail(self, value: int) -> None:
        self.res.append(value)

    def deleteHead(self) -> int:
        if len(self.res) == 0:
            return -1
        while len(self.res) != 0:
            tmp = self.res.pop()
            self.s1.append(tmp)
        tmp = self.s1.pop()
        while len(self.s1) != 0:
            self.res.append(self.s1.pop())
        return tmp

class CQueue:
    """
    更快的提交
    """

    def __init__(self):
        self.A=[]
        self.B=[]

    def appendTail(self, value: int) -> None:
        self.A.append(value)


    def deleteHead(self) -> int:
        if len(self.B)==0:
            if len(self.A)==0:
                return -1
            else:
                self.B[:]=self.A[::-1]
                self.A=[]
                return self.B.pop()
        else:
            return self.B.pop()
# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()