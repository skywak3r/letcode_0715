# -*- coding:utf-8 -*-
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        queue = list()
        dic = {"+","-","*","/"}
        for i in range(len(tokens)):
            if tokens[i] not in dic:
                queue.append(tokens[i])
            else:
                num1 = int(queue.pop())
                num2 = int(queue.pop())
                if tokens[i] == "+":
                    queue.append(num1+num2)
                elif tokens[i] == "-":
                    queue.append(num2 - num1)
                elif tokens[i] == "*":
                    queue.append(num2 * num1)
                else:
                    queue.append(num2 / num1)
        ans = queue[0]
        return int(ans)