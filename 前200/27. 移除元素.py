# -*- coding:utf-8 -*-

"""
python中的while 使用

写代码前想好思路后，再去翻译成代码。


"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        i = 0
        while i < length:
            # print(f"i:{i}")
            if nums[i] == val:
                j = i + 1
                while j < length:
                    nums[j-1] = nums[j]
                    j += 1
                i -= 1
                length -= 1
                # print(nums[:length])
            i += 1
        return length

"""快慢指针

"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast, slow = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
"""
面试中 我写的版本

def deletNum(nums, target):
    l,r = 0, 0
    while r < len(nums):
        while r < len(nums) and nums[r] == target:
            r += 1
        if r >= len(nums):
            break
        nums[l] = nums[r]
        r += 1
        l += 1
    return nums[:l]

"""

"""
优化双指针
因为最后删除的数字是可以乱序的，所以可以把所有删除的数字放在最后的结尾。

面试时候 对变量的定义模糊不清

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums)
        while l < r :
            if nums[l] == val:
                nums[l], nums[r-1] = nums[r-1], nums[l]
                r -= 1
            else:
                l += 1
        return r






"""






