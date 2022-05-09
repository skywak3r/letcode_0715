# -*- coding:utf-8 -*-
class Solution:
    def removeDuplicates(self, s: str) -> str:
        queue = []
        for item in s:
            if not queue:
                queue.append(item)
            elif queue[-1] == item:
                queue.pop()
            else:
                queue.append(item)
        return "".join(queue)