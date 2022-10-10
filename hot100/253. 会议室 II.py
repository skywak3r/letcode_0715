# -*- coding:utf-8 -*-
"""
思路，将开始和结束时间排序，
开始的时候+1
结束的时候-1
统计最多用几个教室
"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        res = [(iv[0],1) for iv in intervals] + [(iv[1],-1) for iv in intervals]
        res.sort()
        ans = 0
        tmp = 0
        for _, i in res:
            tmp += i
            ans = max(ans, tmp )
        return ans