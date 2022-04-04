# -*- coding:utf-8 -*-
"""
正常压入，看pop的值是否是当前栈顶的值，如果是，就pop出来。

最后看是否能把stack pop完


"""
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for num in pushed:
            stack.append(num)
            while stack:
                if stack[-1] == popped[i]:
                    stack.pop()
                    i += 1
                else:
                    break

        return i == len(popped)
