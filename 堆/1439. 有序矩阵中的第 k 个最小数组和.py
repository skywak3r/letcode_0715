# -*- coding:utf-8 -*-
"""
从第一列开始，把所有可能的 都入堆，pop K次就是要的结果。

知识点：
1.使用tuple存储指针，
2. tuple的修改
转为list，再修改，再转为tuple
3.使用hashset存储重复情况
4. 二维数组遍历要想好两个变量由谁控制
"""

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        h = []
        m,n = len(mat),len(mat[0])
        cur = (sum(vec[0] for vec in mat),tuple([0]*m))
        heapq.heappush(h,cur)
        seen = set(cur)
        for _ in range(k):
            acc, pointers = heapq.heappop(h)
            for i,pointer in enumerate(pointers):
                if pointer != n-1:
                    t = list(pointers)
                    t[i] = pointer + 1
                    tt = tuple(t)
                    if tt not in seen:
                        seen.add(tt)
                        heapq.heappush(h, (acc+mat[i][pointer+1]-mat[i][pointer], tt))



        return acc