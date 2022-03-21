# -*- coding:utf-8 -*-
"""
建模成为：假设加法的总和为x，那么减法对应的总和就是sum - x。

x - (sum -x ) =target

####此时有个隐含的条件
若设负数之和为x
sum -x -x = target
x = sum-target / 2
所以sum -target 要大于等于0



**此时问题就转化为，装满容量为x背包，有几种方法**。  因为weight 就是value。 也就等价于 把背包容量为x的背包装满，且value为x  有几种方法

所以求组合类问题的公式，都是类似这种：

```python
dp[j] += dp[j - nums[i]]
```





"""
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if (sum(nums)+target )&1:
            return 0
        bagSize = (sum(nums)+target) >>1

        if abs(target)>sum(nums):
            return 0
        dp = [0] * (bagSize+1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(bagSize, nums[i]-1, -1):
                dp[j] += dp[j-nums[i]]
        return dp[bagSize]
