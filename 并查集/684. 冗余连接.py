# -*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/redundant-connection/solution/rong-yu-lian-jie-by-leetcode-solution-pks2/
定义两个函数。
find  union

"""
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        def find(index):
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]
        def union(index1, index2):
            parent[find(index1)] = find(index2)

        for node1, node2 in edges:
            if find(node1) != find(node2):
                union(node1, node2)
            else:
                return [node1, node2]
        return []
