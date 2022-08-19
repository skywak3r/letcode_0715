# -*- coding:utf-8 -*-

"""
结合题目，有最长这个字眼，可以考虑尝试使用 动态规划 进行分析。这是一个 最值型 动态规划的题目。

动态规划题目分析的 4 个步骤：

确定状态
研究最优策略的最后一步
化为子问题
转移方程
根据子问题定义得到
初始条件和边界情况
计算顺序

dp[i] 表示 s[i] 可以和前面组成有效括号为

if s[i] == (  那就是0
else：
    如果前一个 是 (   那么 dp[i] = dp[i-2] + 2
    如果前一个是  )   那么就要看 dp [i-1] 前面那个是否是(

"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) < 2:
            return 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i] = 2
                    if i >= 2:
                        dp[i] = dp[i-2] + dp[i]
                elif dp[i-1] > 0:  # 如果前一个是 ) ， 当 dp[i] 有值才去计算
                    if i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1 ] == "(":
                        dp[i] = dp[i-1] + 2 + dp[i - dp[i-1] - 2]
        # print(dp)
        return max(dp)

"""
O(1) 空间复杂度的解法， 双指针。 计算left和右边的括号数量


下面 贪心的考虑了 右边括号大于左边，那就归零。
但是会少了一种情况。

(()
left 和right 不会相等，但是答案是2.
所以再倒序走一遍，就可以避免这个情况

"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) < 2:
            return 0
        res = 0
        left, right = 0 , 0
        for i in range(len(s)):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                res = max(res, left * 2)
            elif right > left:
                left = 0
                right = 0
        #
        left, right = 0, 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                res = max(res, left * 2)
            elif right < left:
                left = 0
                right = 0
        return res
