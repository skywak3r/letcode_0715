# -*- coding:utf-8 -*-
"""
建模： 将wordList 视为 完全背包。 将s字符串视为容量。
测试容量为len(s)的 能否正好装 wordList中的值

dp[i] 表示 前i个字符串是否可以装入wordList

如果确定dp[j] 是true，且 [j, i] 这个区间的子串出现在字典里，那么dp[i]一定是true。（j < i ）。

所以递推公式是 if([j, i] 这个区间的子串出现在字典里 && dp[j]是true) 那么 dp[i] = true。


4. 确定遍历顺序
题目中说是拆分为一个或多个在字典中出现的单词，所以这是完全背包。
这道题不是组合也不是排列。所以顺序无关。

但本题还有特殊性，因为是要求子串，最好是遍历背包放在外循环，将遍历物品放在内循环。

所以最终我选择的遍历顺序为：遍历背包放在外循环，将遍历物品放在内循环。内循环从前到后。

这里最重要的是： 由于遍历的时候， 由于会对dp[i] 多次修改， 只需要有一个为True 就可。所以前方需要加上  or dp[i]



"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if i >= len(word):
                    dp[i] = dp[i] or (dp[i - len(word)] and s[i - len(word):i] == word)

        return dp[len(s)]