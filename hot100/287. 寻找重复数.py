# -*- coding:utf-8 -*-
"""
快慢指针 + 环形链表

"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        slow = nums[slow]
        fast = nums[nums[fast]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        pre1 = 0
        pre2 = slow
        while pre1 != pre2:
            pre1 = nums[pre1]
            pre2 = nums[pre2]
        return pre1