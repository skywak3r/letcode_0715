"""
只能往下和右。
想好函数返回什么值
两个方法： 1.函数开始 是否超出范围：超出范围
2.函数开始   是否在范围里
"""

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def split(num):
            cur = num
            src = []
            while cur:
                a = cur % 10

                cur = cur // 10
                src.append(a)
            return sum(src)

        used = [[False] * n for _ in range(m)]

        def dfs(i, j, used):
            if i >= m or j >= n or split(i) + split(j) > k or used[i][j]:
                return 0
            used[i][j] = True
            down = dfs(i, j + 1, used)
            right = dfs(i + 1, j, used)
            ans = 1 + down + right
            return ans

        # print(split(7))

        ans = dfs(0, 0, used)
        return ans

"""
bfs
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def split(num):
            cur = num
            src= []
            while cur:
                a = cur % 10 

                cur = cur//10
                src.append(a)
            return sum(src)
        que = collections.deque()
        que.append((0,0))
        path = set()
        while que:
            i,j = que.popleft()
            if (i,j) not in path  and split(i) + split(j) <=k:
                path.add((i,j))
                for x,y in [(i+1,j),(i,j+1)]:
                    if 0<=x<m and 0<=y<n:
                        que.append((x,y))
        return len(path)
"""