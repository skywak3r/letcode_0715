# -*- coding:utf-8 -*-

###不能重复：使用了used。
###在for循环的时候，是从头到尾。和39不同

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, begin, end,tmp, src,used):
            if len(tmp) == len(nums):
                src.append(tmp.copy())
            for i in range(0,end):
                if used[i] == False:
                    tmp.append(nums[i])
                    used[i] = True
                    # print(f"i:{i},tmp:{tmp}")

                    # print(f"used[{i}]:{used[i]}")
                    # print(f"begin:{begin}")
                    backtrack(nums,begin+1,end,tmp, src ,used)
                    used[i]=False

                    tmp.pop()
        tmp, src = [], []
        used = [False for _ in range(len(nums))]
        backtrack(nums, 0, len(nums), tmp, src,used)
        return src
