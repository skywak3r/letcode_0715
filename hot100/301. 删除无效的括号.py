# -*- coding:utf-8 -*-
"""
bfs的方法：
第一层表示删除了一个括号的所有集合。
第二次表示删除了两个
https://leetcode.cn/problems/remove-invalid-parentheses/solution/bfsjian-dan-er-you-xiang-xi-de-pythonjiang-jie-by-/


"""


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s):
            cnt = 0
            for c in s:
                if c == "(":
                    cnt += 1
                elif c == ")":
                    cnt -= 1
                if cnt < 0:
                    return False
            return cnt == 0

        level = {s}
        while True:
            valid = list(filter(isValid, level)) # 过滤出有效的。
            if valid:
                return valid
            next_level = set() #如果没有 有效的，那就进入下一层。再删一个括号
            for item in level:
                print(level)
                for i in range(len(item)):
                    if item[i] in "()":
                        next_level.add(item[:i] + item[i + 1:])

            level = next_level
