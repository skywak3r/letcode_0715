# -*- coding:utf-8 -*-

快慢指针，如果快指针指的地方不是val，那么快慢指针一起往前走
如果相等，慢指针不动，快指针往前走。

class Solution:
    """双指针法
    时间复杂度：O(n)
    空间复杂度：O(1)
    """

    @classmethod
    def removeElement(cls, nums: List[int], val: int) -> int:
        fast = slow = 0
        while fast<len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
