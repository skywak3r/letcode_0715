# -*- coding:utf-8 -*-
"""
用哈希表存储每个端点值对应连续区间的长度

每次去取 num-1 和num+1的 最长值。


"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        hashTable = dict()
        hashTable = collections.defaultdict(int)
        for num in nums:
            if hashTable[num] == 0:
                # left = hashTable.get(num-1, 0)
                # right =  hashTable.get(num+1, 0)

                # print(num, left, right)
                left = hashTable[num - 1]
                right = hashTable[num + 1]
                # print(num, left, right)
                cur_length = 1 + right + left
                if cur_length > max_length:
                    max_length = cur_length
                hashTable[num] = cur_length
                hashTable[num - left] = cur_length
                hashTable[right + num] = cur_length
        print(hashTable)
        return max_length
