# -*- coding:utf-8 -*-

先拓展空间，再倒序用双指针修改。
左边指针只想原来的结尾。
右边指针只想拓展后的结尾


s = "we are happy"
# def replaceSpace(s):
count = s.count(" ")

res = list(s)
res.extend([" "] * 2 * count )
# print(res)
left = len(s)-1
right = len(res) -1

while left>=0:
    if res[left]!=" ":
        res[right] = res[left]
        right -= 1
    else:
        res[right-2:right+1] = '%20'
        right -= 3
    left -= 1
    # fast += 1



print(res)