# -*- coding:utf-8 -*-
"""
只有50个数据。
思路：
分别计算出从高到低的点之间的距离，然后求和就是结果。
按照 height高低排序好。
使用bfs求出距离。

"""

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        def bfs(x, y, nx, ny):
            steps = 0
            queue = collections.deque()
            queue.append((x, y))
            visited = set()
            visited.add((x, y))
            dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            while queue:
                size = len(queue)
                for _ in range(size):
                    curX, curY = queue.popleft()
                    if curX == nx and curY == ny:
                        return steps
                    for d in dirs:
                        newX = curX + d[0]
                        newY = curY + d[1]
                        if 0 <= newX < M and 0 <= newY < N and forest[newX][newY] != 0 and (
                                (newX, newY) not in visited):
                            queue.append((newX, newY))
                            visited.add((newX, newY))
                steps += 1
            return -1

            # if nx == x and ny == y:
            #     return 0
            # dis = 0
            # queue = collections.deque()
            # seen = [[False] * n for _ in range(m)]
            # seen[x][y] = True
            # queue.append([x,y])
            # while queue:
            #     length = len(queue)
            #     for i in range(length):
            #         curx, cury = queue.popleft()
            #         for direction in dirs:
            #             newX = curx + direction[0]
            #             newY = cury + direction[1]
            #             if not (0 <= newX < m) or not(0 <= newY < n) :
            #                 continue
            #             if forest[newY][newY] == 0 or seen[newX][newY]:
            #                 continue
            #             if newX == nx and newY == ny:
            #                 return dis + 1

            #             queue.append([newX, newY])
            #             print(queue)
            #             seen[newX][newY] = True
            #     dis += 1
            # return -1

        # m,n = len(forest), len(forest[0])
        # res = []
        # for i in range(m):
        #     for j in range(n):
        #         if forest[i][j] > 1:
        #             res.append((forest[i][j], i, j))
        # res.sort()
        # ans = 0
        # x, y = 0, 0
        # dirs = [[0,1],[0,-1],[-1,0],[1,0]]
        # for tmp in res:
        #     nx, ny = tmp[1:]
        #     d = bfs(x,y, nx, ny)
        #     if d == -1:
        #         return -1
        #     ans += d
        #     nx, ny = x, y
        # return ans
        M = len(forest)
        N = len(forest[0])
        trees = []
        for i in range(M):
            for j in range(N):
                if (forest[i][j] > 1):
                    trees.append((forest[i][j], i, j))
        trees.sort()
        preX, preY = 0, 0
        res = 0
        for height, curX, curY in trees:
            steps = bfs(preX, preY, curX, curY)
            if steps == -1:
                return -1
            res += steps
            preX, preY = curX, curY
        return res




