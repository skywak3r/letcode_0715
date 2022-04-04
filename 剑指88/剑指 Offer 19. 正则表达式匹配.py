# -*- coding:utf-8 -*-
"""
常规方法：
无法判断是否完全匹配。
aaa
aa
无法判断是否匹配完

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        length_s, length_p = len(s), len(p)
        if length_s == 0 and length_p == 0:
            return True
        if length_p == 0:
            return False
        count = 0
        for i in range(length_p):
            for j in range(i, length_s):
                if i + 1 < length_p:
                    if p[i + 1] == '*':
                        if p[i] == s[j]:
                            count += 1
                            continue
                        break
                if 'a' <= p[i] <= 'z':
                    if s[j] != p[i]:
                        return False

                    count += 1
                    break
                elif p[i] == '.':
                    if i + 1 < length_p:
                        if p[i + 1] == "*":
                            return True
                    count += 1
                    break
                elif p[i] == '*':
                    break
                # elif p[i] == '*':
                #     if p[i-1] == s[j]:
                #         continue
        return count == length_s
"""
"""
dp

1.dp[i][j 表示s[i-1 p[j-1 是否匹配。
2. （1）如果不是 *
好说
（2）如果是*  分为两种情况 是字母或“.”
如果是字母分为两种情况：出现0次， 出现多次。

(3)初始化。 dp[0[0 = True
当s为空串，p为 * 的时候，为True


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s)+1, len(p) + 1

        dp = [[False] *n for _ in range(m)]
        dp[0][0] = True
        for j in range(2,n,2):
            dp[0][j] = dp[0][j-2] and p[j-1] == "*"
        for i in range(1,m):
            for j in range(1,n):
                if p[j-1] != '*':
                    if dp[i-1][j-1] and s[i-1]==p[j-1]:
                        dp[i][j] = True
                    elif dp[i-1][j-1] and p[j-1] == ".":
                        dp[i][j] = True
                else:
                    if dp[i][j-2]:
                        dp[i][j] = True
                    elif dp[i-1][j] and s[i-1] == p[j-2]:
                        dp[i][j] = True
                    elif dp[i-1][j] and p[j-2] == ".":
                        dp[i][j] = True
        return dp[-1][-1]


"""