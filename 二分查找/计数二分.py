# -*- coding:utf-8 -*-
"""
答案不对
https://binarysearch.com/problems/Kth-Pair-Distance
"""
class Solution:
    def solve(self, nums, k):
        def countN(diff):
            src = 0
            # print(1)
            for i in range(length-1):
                for j in range(i + 1, length):
                    if nums[j] - nums[i] <= diff:
                        src += 1
            # print(f"src:{src}")
            # print(src>=k)
            return src >= k
        nums.sort()
        l, r = 0, max(nums) - min(nums)

        ans = float('inf')
        length = len(nums)

        while l <= r:
            # print(f"ans:{ans}")
            # print(f"l:{l},r:{r}")
            diff = l + (r - l)/2
            # print(f"diff:{diff}")
            # print(f"r:{r}")
            if countN(diff):
                # print(1)
                ans = min(ans, diff)
                # print(f"ans:{ans}")
                r = diff - 1
                # print(f"r:{r}")

            else:
                # print(f"l:{l}")
                l = diff + 1
        return ans







