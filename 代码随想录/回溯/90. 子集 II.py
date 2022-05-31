# -*- coding:utf-8 -*-
""""""
"""
元素有重复， 但是求出的组合不能有重复。
含义： 同一颗树，如果有重复元素，可以重复拿。但是同一层不可以拿。
两个解决方法：1. 使用index 控制。  先sort一下，后续 如果 i > index 并且 nums[i] == nums[i-1] 就说明是同层的了。要continue掉
2. 使用used数组。 当nums[i-1] == nums[i] 并且 used[i-1] == false （前一个树上没有使用那个数字。说明这一层肯定要使用了。
"""


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        path = []
        ans = []

        def backtrack(index, path):
            ans.append(path[:])
            if index >= len(nums):
                return
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, path)

        return ans