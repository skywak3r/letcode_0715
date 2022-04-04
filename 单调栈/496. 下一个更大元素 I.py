# -*- coding:utf-8 -*-
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)
        stack = [0]
        for i in range(1, len(nums2)):
            if nums2[i] <= nums2[stack[-1]]:
                stack.append(i)
            else:
                while (len(stack) != 0 ) and (nums2[i] > nums2[stack[-1]]):
                    if nums2[stack[-1]] in nums1:
                        index = nums1.index(nums2[stack[-1]])
                        ans[index] = nums2[i]
                    stack.pop()
                stack.append(i)
        return ans


"""
4.4号写

正常遍历nums2.只有当遍历的值在nums1中，才去记录。

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)
        stack = [0]
        for i in range(1,len(nums2)):
            if nums2[i] <= nums2[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) != 0 and nums2[i] > nums2[stack[-1]]:
                    if nums2[stack[-1]] in nums1:
                        index = nums1.index(nums2[stack[-1]])
                        ans[index] = nums2[i]

                    stack.pop()
                stack.append(i)
        return ans             
"""