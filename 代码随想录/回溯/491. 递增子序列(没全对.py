# -*- coding:utf-8 -*-
""""""
"""
未全面考虑重复元素。问题的关键还是：同层不能出现同样的元素。
[1,2,1,1]
因为这里的数组不能sort。所以不能单使用 nums[i-1] == nums[i]去控制重复
下方代码：构造好整个path之后看是否有重复。 优于30%

更优的办法是：在本层用一个set控制是否重复。  优于50%

"""
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        seen = set()
        def backtrack(index, path):
            if len(path) >= 2:
                if tuple(path) not in seen:
                    ans.append(path[:])
                    seen.add(tuple(path))
            if index >= len(nums):
                return
            for i in range(index, len(nums)):
                if i > index and nums[i-1] == nums[i]:
                    continue
                if not path:
                    path.append(nums[i])
                elif path[-1] <= nums[i]:
                    path.append(nums[i])
                else:
                    continue
                backtrack(i + 1, path)
                path.pop()
        backtrack(0, path)
        return ans