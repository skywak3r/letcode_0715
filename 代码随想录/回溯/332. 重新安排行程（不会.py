# -*- coding:utf-8 -*-
""""""
"""
难点：建模和抽象问题

为什么要有返回值呢？ 因为在递归的时候是要找到一条路
"""
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ticketsDic = defaultdict(list)
        for ticket in tickets:
            ticketsDic[ticket[0]].append(ticket[1]) #把机票做成列表形式
        # print(ticketsDic)
        path = ["JFK"]
        def backtrack(start):
            if len(path) == len(tickets) + 1:
                return True
            ticketsDic[start].sort()  #保证有序输出
            for _ in ticketsDic[start]:   #相当于 回溯的横着走
                endPoint = ticketsDic[start].pop(0)   #去除掉要走的，减少第二层的可选数量。
                path.append(endPoint)
                if backtrack(endPoint):
                    return True
                path.pop()
                ticketsDic[start].append(endPoint)
        backtrack("JFK")
        return path
