# -*- coding:utf-8 -*-
"""
对数组原地修改，并且减小移动的次数，就要从末尾开始移动

从末尾修改，用双指针


"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tail = m + n - 1
        p1, p2 = m - 1, n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                tail -= 1
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                tail -= 1
                p2 -= 1
        while p1 >= 0:
            nums1[tail] = nums1[p1]
            tail -= 1
            p1 -= 1
        while p2 >= 0:
            nums1[tail] = nums2[p2]
            tail -= 1
            p2 -= 1


"""
时间复杂度是o(n) 空间复杂度也是

"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        src = []
        p1, p2 = 0, 0
        while p1 < m and p2 < n:
            if nums1[p1] < nums2[p2]:
                src.append(nums1[p1])
                p1 += 1
            else:
                src.append(nums2[p2])
                p2 += 1
        while p1 < m:
            src.append(nums1[p1])
            p1 += 1
        while p2 < n:
            src.append(nums2[p2])
            p2 += 1
        for i in range(len(src)):
            nums1[i] = src[i]
        # nums1 = src.copy()
