# -*- coding:utf-8 -*-
"""
1.用堆存储最高的差距， 如果砖头不够用了， 再去把最大的高差用梯子替换掉。
2. 一定要先把砖头减去，再去判断，否则就会漏掉当前的diff


"""
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        max_diff = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff < 0:
                continue
            else:
                bricks -= diff
                heapq.heappush(max_diff, -diff)
                if bricks < 0:

                    if ladders > 0:
                        ladders -= 1

                        bricks -= heapq.heappop(max_diff)
                    else:
                        return i
                else:
                    continue

        return len(heights) - 1


