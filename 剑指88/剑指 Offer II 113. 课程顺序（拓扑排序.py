# -*- coding:utf-8 -*-

"""
1. 构造个图 和 每个点的 入度数组

2. 首先把入度为0的 入队列

3. 广度优先搜索。
pop出队列中最早的点u， 加入结果

把以u为起点能到达的节点的 度  减一  （相当于删除了该节点到别的节点的边了

遍历u能到达的节点，看有没有  入度为0的，有的话加入队列


下面是BFS的答案
"""

import collections
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = collections.defaultdict(list)
        indeg = [0] * numCourses
        result = list()
        for info in prerequisites:
            edges[info[1]].append(info[0])
            indeg[info[0]] += 1
        q = deque()
        for i in range(len(indeg)):
            if indeg[i] == 0:
                q.append(i)
        while q:
            u = q.popleft()
            result.append(u)
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        print(result)
        if len(result) != numCourses:
            result = []
        return result



