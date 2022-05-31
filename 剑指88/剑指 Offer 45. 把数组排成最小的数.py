# -*- coding:utf-8 -*-
"""
两个方法：
 库函数：functools.cmp_to_key
手写快排:
定 排序判断规则 为：

若拼接字符串 x + y > y + x x+y>y+x ，则 xx “大于” yy ；
反之，若 x + y < y + x x+y<y+x ，则 xx “小于” yy ；
xx “小于” yy 代表：排序完成后，数组中 xx 应在 yy 左边；“大于” 则反之。

根据以上规则，套用任何排序方法对 numsnums 执行排序即可。




"""
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        newNums = [str(num) for num in nums]
        # def cmp(a,b):
        #     if int(a + b) >= int(b+a):
        #         return 1
        #     else:
        #         return -1
        # newNums = sorted(newNums, key = functools.cmp_to_key(cmp))
        # return "".join(newNums)
        def partital(nums, left, right):
            i, j = left, right
            while i < j:
                while i < j and nums[i] + nums[j] <= nums[j] + nums[i] :
                    j -= 1
                while i < j and nums[i] + nums[j] <= nums[j] + nums[i]:
                    i += 1
                nums[i],nums[j] = nums[j], nums[i]
            return i
        def quicksort(nums, left, right):
            if left < right :
                index = partital(nums, left, right)
                quicksort(nums, left, index-1)
                quicksort(nums, index + 1, right)
        quicksort(newNums, 0, len(nums)-1)
        return "".join(newNums)