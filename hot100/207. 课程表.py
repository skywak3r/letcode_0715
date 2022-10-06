# -*- coding:utf-8 -*-
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        need = collections.defaultdict(list)
        for course, pre in  prerequisites:
            need[pre].append(course)
            indegree[course] += 1
        stack = collections.deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                stack.append(i)
        while stack:
            cur = stack.popleft()
            numCourses -= 1
            nxt = need[cur]
            for c in nxt:
                indegree[c] -= 1
                if indegree[c] == 0:
                    stack.append(c)
        return not numCourses
