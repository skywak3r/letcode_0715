# -*- coding:utf-8 -*-
"""
方法一： 暴力法，但是会超时

n2的复杂度， 一旦比n2复杂度大， 就可以无伤排序

既然排序了， 去重之后就可以用二分了

"""
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                heapq.heappush(heap, abs(nums[i] - nums[j]))
        for i in range(k):
            cur = heapq.heappop(heap)
        return cur


"""
对二分查找的key 魔改

排序后，差值肯定在最大值到最小值之间。  
计算mid 属于排名第几



"""
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        nums = sorted(nums)
        n = len(nums)
        def count(mid):
            #为了计算小于mid的有几个

            right = 0
            cnt = 0
            for left in range(n):
                while right < n and nums[right] - nums[left] <= mid:
                    right += 1
                    cnt += right - left - 1
            return cnt

        low = 0
        upper = nums[-1] - nums[0]
        while low < upper:
            mid = (low + upper) // 2
            r = count(mid)
            if r >= k:
                upper = mid
            else:
                low = mid + 1

        return low

作者：lnnnnnnn
链接：https://leetcode.cn/problems/find-k-th-smallest-pair-distance/solution/-by-lnnnnnnn-4id1/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。