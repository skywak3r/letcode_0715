# -*- coding:utf-8 -*-
class MinStack:
    """
    剑指 Offer 30. 包含 min 函数的栈
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

 

示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.


    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.minNum = float("inf")
        self.topNum = 0
        self.length = 0

    def push(self, x: int) -> None:
        self.s.append(x)
        self.length += 1
        self.topNum = x

        if x <= self.minNum:
            self.minNum = x

    def pop(self) -> None:
        tmp = self.s.pop()
        self.length -= 1
        if self.length == 0:
            self.topNum = False
            self.minNum = float("inf")
        else:
            self.topNum = self.s[self.length - 1]
            self.minNum = min(self.s)

    def top(self) -> int:
        return self.topNum

    def min(self) -> int:
        return self.minNum

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()