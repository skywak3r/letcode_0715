from bisect import bisect_left,bisect_right
import bisect
from collections import defaultdict
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        dp = [False  for _ in range(len(s)+1)]
        dp[0] = True
        for i in range(len(wordDict)):
            for j in range(len(wordDict[i]), len(s)+1, 1):
                dp[j] = dp[j-len(wordDict[i])] and s[j-len(wordDict[i]):j] == wordDict[i]
        print(dp)
        return dp[-1]

if __name__ =="__main__":
    # a = Solution()
    # s = "leetcode"
    # dic = ["leet","code"]
    # a.wordBreak(s,dic)
    a = defaultdict(int)

    print(a['1'])