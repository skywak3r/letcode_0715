# -*- coding:utf-8 -*-
""""""
"""
下面的方法不好。不容易掌握

对于数组问题，如果寻找连续子数组，可以使用双指针法或滑动窗口等方法，但是对于非连续子数组，最好使用动态规划。
dp 代表以j 为结尾，step 的长度
字典构成dp
dict.get() 第二个参数是默认返回值



暴力法  n3次方

三次方以上的复杂度，想想能不能用字典记录一些不用另外走的。

"""
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        # ans = 1
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         d = nums[i] - nums[j]
        #         count = 2
        #         cur = nums[j]
        #         r = j + 1
        #         while r < len(nums):
        #             if nums[r] == cur - d:
        #                 count += 1
        #                 cur = nums[r]
        #             r += 1
        #             ans = max(ans, count)
        #         if ans == len(nums):
        #             return len(nums)
        # return ans
        dp = dict()
        for end in range(1, len(nums)):
            for previous in range(end):
                step = nums[end] - nums[previous]
                dp[(end,step)] = dp.get((previous, step), 1) + 1
        return max(dp.values())


"""
这种方法好理解。
将等差数量全部搞成正数
dp[i][d] 表示 第i个数字，与前面的数相差为d的最长等差子数列

class Solution {
    public int longestArithSeqLength(int[] nums) {
        int n = nums.length, ans = 0;
        int[][] dp = new int[n][1010];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                // 表示nums[i]与nums[j]以差为d构成等差数列
                int d = nums[i] - nums[j] + 500;
                // dp[i][d]表示：nums[i]以差为d能与前面的数构成的等差数列的长度
                dp[i][d] = Math.max(dp[i][d], dp[j][d] + 1);
                ans = Math.max(ans, dp[i][d]);
            }
        }
        return ans + 1;
    }
}


"""

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:

        ans = 0
        dp = [[0] * 1010 for _ in range(len(nums))]

        for i in range(len(nums)):
            for j in range(i):
                d = nums[i] - nums[j] + 500
                dp[i][d] = max(dp[i][d], dp[j][d]+1)
                ans = max(ans, dp[i][d])
        return ans + 1