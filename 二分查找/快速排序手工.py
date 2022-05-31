# -*- coding:utf-8 -*-
def partition(nums, left, right):
    #把base Num 放在了该放的位置上，并且返回他的下标。用于切分数组
    baseNum = nums[left]
    i, j = left, right
    while i < j:
        while i<j and nums[j] >= baseNum:
            j -= 1
        nums[i] = nums[j]
        while i < j and nums[i] <= baseNum:
            i += 1
        nums[j] = nums[i]
    nums[i] = baseNum
    return i

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

nums = [10,9,8,1,-2,10,8,4]
quicksort(nums,0, len(nums) -1)
print(nums)
