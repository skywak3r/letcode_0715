# -*- coding:utf-8 -*-
"""

https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/solution/mian-shi-ti-33-er-cha-sou-suo-shu-de-hou-xu-bian-6/
二叉搜索树 后序遍历：
左树|右边|根

思路：找到左右子树的分界点。
找到第一个大于根的值即为m

分为 i m-1    m - j
继续分



"""
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def recur(i,j):
            if i >= j:
                return True
            p = i
            while postorder[p] < postorder[j]:
                p+= 1
            m = p
            while postorder[p] > postorder[j]:
                p += 1
            return p ==j and recur(i,m-1) and recur(m,j-1)
        return recur(0, len(postorder)-1)
