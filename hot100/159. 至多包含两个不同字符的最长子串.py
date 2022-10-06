# -*- coding:utf-8 -*-
"""
滑动窗口
https://leetcode.cn/problems/longest-substring-with-at-most-two-distinct-characters/solution/hua-dong-chuang-kou-zhen-di-jian-dan-yi-73bii/

合集



"""

"""
class Solution:
    def problemName(self, s: str) -> int:
        # Step 1: 定义需要维护的变量们 (对于滑动窗口类题目，这些变量通常是最小长度，最大长度，或者哈希表)
        x, y = ..., ...

        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0
        for end in range(len(s)):
            # Step 3: 更新需要维护的变量, 有的变量需要一个if语句来维护 (比如最大最小长度)
            x = new_x
            if condition:
                y = new_y

            '''
            ------------- 下面是两种情况，读者请根据题意二选1 -------------
            '''
            # Step 4 - 情况1
            # 如果题目的窗口长度固定：用一个if语句判断一下当前窗口长度是否超过限定长度
            # 如果超过了，窗口左指针前移一个单位保证窗口长度固定, 在那之前, 先更新Step 1定义的(部分或所有)维护变量
            if 窗口长度大于限定值:
                # 更新 (部分或所有) 维护变量
                # 窗口左指针前移一个单位保证窗口长度固定

            # Step 4 - 情况2
            # 如果题目的窗口长度可变: 这个时候一般涉及到窗口是否合法的问题
            # 如果当前窗口不合法时, 用一个while去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法
            # 在左指针移动之前更新Step 1定义的(部分或所有)维护变量
            while 不合法:
                # 更新 (部分或所有) 维护变量
                # 不断移动窗口左指针直到窗口再次合法

        # Step 5: 返回答案
        return ...
"""

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        max_len, hashMap = 0, {}
        start = 0
        for end in range(len(s)):
            tail = s[end]
            hashMap[tail] = hashMap.get(tail,0) + 1
            if len(hashMap) <= 2:
                max_len = max(max_len, end - start +1)
            while len(hashMap) > 2:
                head = s[start]
                hashMap[head] -= 1
                if hashMap[head] == 0:
                    del hashMap[head]
                start += 1
        return max_len
