# -*- coding:utf-8 -*-
# def partition(nums, left, right):
#     #把base Num 放在了该放的位置上，并且返回他的下标。用于切分数组
#     baseNum = nums[left]
#     i, j = left, right
#     while i < j:
#         while i<j and nums[j] >= baseNum: # 从右边找一个basenum小的值
#             j -= 1
#         nums[i] = nums[j]# 把找到那个小值，放在left
#         while i < j and nums[i] <= baseNum:  #从左边找一个比basenum大的值
#             i += 1
#         nums[j] = nums[i] #把大的值放在右边
#     nums[i] = baseNum  # 把basenum放在合适的位置上
#     return i

def partition(nums, left, right):
    baseNum = nums[left]
    l, r = left, right
    while l < r:
        while l< r and nums[r] >= baseNum:
            r -= 1
        nums[l] = nums[r]
        while l < r and nums[l] <= baseNum:
            l += 1
        nums[r] = nums[l]
    nums[l] = baseNum
    return l

#快速排序
def quicksort(nums, left, right):
    # print(nums)
    # if left < right:
    #     index = partition(nums, left, right)
    #     quicksort(nums, left, index-1)
    #     quicksort(nums, index + 1, right)
    if left < right:
        index = partition(nums, left, right)
        quicksort(nums, left, index-1)
        quicksort(nums, index+1, right)




# def partition(nums, left, right):
#     baseNum = nums[left]
#     i, j = left, right
#     while i < j :
#         while i < j and nums[j] >= baseNum:
#             j -= 1
#         nums[i] = nums[j]
#         while i < j and nums[i] <= baseNum:
#             i += 1
#         nums[j] = nums[i]
#     nums[i] = baseNum
#     return i


nums = [10,9,8,1,-2,10,8,4]
quicksort(nums,0, len(nums) -1)
print(nums)