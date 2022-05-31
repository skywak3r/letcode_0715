# -*- coding:utf-8 -*-
""""""

"""
核心是下方去重代码：代表前一个使用过了 相同的数字，那么当前这个数字就不用了。是属于树枝剪枝。
                if i > 0 and nums[i-1] == nums[i] and used[i-1] :
                    continue
树层剪枝：
                if i > 0 and nums[i-1] == nums[i] and not used[i-1] :
                    continue
            // used[i - 1] == true，说明同一树枝nums[i - 1]使用过
            // used[i - 1] == false，说明同一树层nums[i - 1]使用过
            // 如果同一树层nums[i - 1]使用过则直接跳过


"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        path = []
        used = [False] *len(nums)
        def backtrack(path, used):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            for i in range(len(nums)):
                if i > 0 and nums[i-1] == nums[i] and used[i-1] and not used[i]:
                    continue
                if not used[i]:
                    path.append(nums[i])
                    used[i] = True
                    backtrack(path, used)
                    used[i] = False
                    path.pop()
        backtrack(path, used)
        return ans
