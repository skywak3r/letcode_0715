# -*- coding:utf-8 -*-
""""""
"""
1.当复杂度超过n2  能排序就排序。
2. 遍历每一个节点， 以节点后方的数组 做二分查找。
二分查找的代码：https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247484507&idx=1&sn=36b8808fb8fac0e1906493347d3c96e6&source=41#wechat_redirect



"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    while (l < r) and nums[l] == nums[l + 1]:
                        l += 1
                    while (l < r) and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return ans


