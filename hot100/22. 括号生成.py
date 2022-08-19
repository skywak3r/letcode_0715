# -*- coding:utf-8 -*-
"""
难点是： 迭代的控制。
没想好用那个变量去迭代。


要用左右括号剩下的个数去遍历。。
下方 递归法：
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def getParenthesis(s, left, right):
            if left == 0 and right == 0:  # 定义返回条件
                res.append(s)
                return
            if left == right:   #如果左右相当，我需要先加个左括号
                getParenthesis(s+"(", left - 1, right)
            elif left < right: # 如果右边大，那么左右都可以
                if left > 0 :
                    getParenthesis(s+"(", left -1, right)
                getParenthesis(s + ")", left, right- 1)
        if n < 0:
            return res
        getParenthesis("", n, n)
        return res


"""
下方会回溯法
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def backtrack(path, left, right):
            if len(path) == 2*n:
                res.append("".join(path[:]))
                return
            if left < n:
                path.append("(")
                backtrack(path, left+1, right)
                path.pop()
            if left > right:
                path.append(")")
                backtrack(path,left,right+1)
                path.pop()
        backtrack(path, 0, 0)
        return res


