# -*- coding:utf-8 -*-
""""""
"""

void backtracking(参数) {
    if (终止条件) {
        存放结果;
        return;
    }

    for (选择：本层集合中元素（树中节点孩子的数量就是集合的大小）) {
        处理节点;
        backtracking(路径，选择列表); // 递归
        回溯，撤销处理结果
    }
}

"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(n, k, index, path):
            if len(path) == k:
                ans.append(path.copy())
                return
            for i in range(index, n+1):
                path.append(i)
                backtrack(n, k, i+1, path)
                path.pop()
        ans = []
        path = []
        backtrack(n, k, 1, path)
        return ans