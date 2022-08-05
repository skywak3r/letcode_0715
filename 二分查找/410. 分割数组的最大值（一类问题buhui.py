# -*- coding:utf-8 -*-
"""
https://leetcode.cn/problems/split-array-largest-sum/solution/er-fen-cha-zhao-by-liweiwei1419-4/
题目中看到了
尤其是「非负整数数组」和「连续」这两个信息


最重要的是 mid计算的时候要向下取整，并且


思路： 不断切分数组，找到 切分数组各自和的最大值  的最小值。 看上面的网址最好


练习
这些问题都如出一辙，请大家特别留意题目中出现的关键字「非负整数」、分割「连续」，思考清楚设计算法的关键步骤和原因，相信以后遇到类似的问题就能轻松应对。

「力扣」第 875 题：爱吃香蕉的珂珂（中等）
LCP 12. 小张刷题计划 （中等）
「力扣」第 1482 题：制作 m 束花所需的最少天数（中等）
「力扣」第 1011 题：在 D 天内送达包裹的能力（中等）
「力扣」第 1552 题：两球之间的磁力（中等）


"""
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums), sum(nums)
        def split(nums, mid):
            #把nums 分块，使得分块的和最大值不超过mid
            length = len(nums)
            res = 1
            curSum = 0
            for i in range(length):
                tmp = curSum + nums[i]
                if tmp <= mid: # 注意这里有等号
                    curSum = tmp
                else:
                    curSum = nums[i]
                    res += 1
            return res

        while left < right:
            mid = int(left + (right - left) / 2)
            splits = split(nums, mid)
            # print(splits)
            if splits > m :
                left = mid + 1
            else:
                right = mid
        return left




"""
public class Solution {

    public int splitArray(int[] nums, int m) {
        int max = 0;
        int sum = 0;

        // 计算「子数组各自的和的最大值」的上下界
        for (int num : nums) {
            max = Math.max(max, num);
            sum += num;
        }

        // 使用「二分查找」确定一个恰当的「子数组各自的和的最大值」，
        // 使得它对应的「子数组的分割数」恰好等于 m
        int left = max;
        int right = sum;
        while (left < right) {
            int mid = left + (right - left) / 2;

            int splits = split(nums, mid);
            if (splits > m) {
                // 如果分割数太多，说明「子数组各自的和的最大值」太小，此时需要将「子数组各自的和的最大值」调大
                // 下一轮搜索的区间是 [mid + 1, right]
                left = mid + 1;
            } else {
                // 下一轮搜索的区间是上一轮的反面区间 [left, mid]
                right = mid;
            }
        }
        return left;
    }

"""