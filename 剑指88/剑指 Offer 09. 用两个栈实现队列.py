# -*- coding:utf-8 -*-
##使用 st1 存储刚加入的
#使用st2 存储要删除的
#

class CQueue:

    def __init__(self):
        self.st1 = []
        self.st2 = []

    def appendTail(self, value: int) -> None:
        self.st1.append(value)

    def deleteHead(self) -> int:
        if self.st2:
            return self.st2.pop()
        if not self.st1:
            return -1
        while self.st1:
            self.st2.append(self.st1.pop())
        return self.st2.pop()
