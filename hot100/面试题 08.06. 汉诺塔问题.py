# -*- coding:utf-8 -*-
"""
递归问题：

把问题拆解成白话文，
再用程序语言去翻译。

如果一下子移动n个太复杂，那就从头开始看

n = 1
直接从A 移动到C就好了

n = 2
把 1 个 移动到b， 剩下一个移动到c

n = 3
把2 个移动到b， 剩下一个移动到c



难点，用什么变量去控制变量往前推进

"""


class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        length = len(A)
        self.move(length, A, B, C)    # 把A的length个通过B移动给C

    def move(self, n, A, B, C):
        if n == 1: #如果只有一个，那么直接把A放过去就好了
            C.append(A[-1])
            A.pop()
            return
        else:
            self.move(n - 1, A, C, B)  # 先把n-1个的A，通过C移动到B
            C.append(A[-1])  # 把A剩下的一个直接移动给C
            A.pop()
            self.move(n - 1, B, A, C)  # 把n-1个B 通过A移动给C

