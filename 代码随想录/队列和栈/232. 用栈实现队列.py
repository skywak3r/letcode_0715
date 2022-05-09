# -*- coding:utf-8 -*-
""""""
"""
有两个队列
push的时候，往 in里面放。
pop的时候，先从out中 pop。如果out为空。 就把in里面的全部放进out，再去pop


"""
class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []
    def push(self, x: int) -> None:
        self.stack_in.append(x)
    def pop(self) -> int:
        if self.empty():
            return None
        if self.stack_out:
            return self.stack_out.pop()
        else:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()
    def peek(self) -> int:
        ans = self.pop()
        self.stack_out.append(ans)
        return ans
    def empty(self) -> bool:
        if not self.stack_in and not self.stack_out:
            return True
        else:
            return False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()