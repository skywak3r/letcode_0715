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
