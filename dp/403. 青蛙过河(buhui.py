# -*- coding:utf-8 -*-
""""""
"""
dfs
从第一个节点 一个一个遍历
给出的nums 是 陆地所在的位置。  （审题不清楚就开始想题

"""

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        @lru_cache(None)
        def dfs(pos, step):
            if pos == stones[-1]:   return True
            for d in [-1, 0, 1]:
                if step + d > 0 and pos + step + d in stones:
                    if dfs(pos + step + d, step + d):
                        return True
            return False
        pos, step = 0, 0
        return dfs(pos,step)

"""
dp
第一个是到达第i个为位置。
第二个是 到达位置i 走了k步

其中 k  = stones[i] - stones[j]

范围问题：
因为步数每次增加1，所以步数最多为 len(stones)+ 1 

所以在第j 个点的时候  
k 一定小于等于 J - 1
"""

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        length = len(stones)
        dp = [[False] * length for _ in range(length)]
        dp[0][0] = True

        for i in range(1, length):
            for j in range(0, i):
                k = stones[i] - stones[j]
                if k <= j + 1 :
                    dp[i][k] = dp[j][k-1] or dp[j][k] or dp[j][k+1]
        return any(dp[-1])

"""
        # 方法二： 动态规划
        把dp设计为能够到达 i 的 k 的集合
        set_stones = set(stones)

        dp = defaultdict(set)
        dp[0] ={0}
        for s in stones:
            for step in dp[s]:
                for d in [1,-1,0]:
                    if step + d > 0 and s + step + d in set_stones:
                        dp[s + step + d].add(step + d)
        return len(dp[stones[-1]]) > 0
"""