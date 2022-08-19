# -*- coding:utf-8 -*-
A = [5,19,8,1]

def solution(A):
    import heapq
    total = sum(A)
    target = total / 2
    heap = []
    heapq.heapify(A)
    cur = 0
    res = 0
    while cur < target:
        curMax = heapq.heappop(A) / 2
        cur += curMax
        heapq.heappush(A, curMax)
        res += 1
    return res
print(solution(A))


