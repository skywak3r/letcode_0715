nums = [3,3]
target = 6
for i in range(len(nums)):
    remain = target - nums[i]
    if remain in nums[i + 1:]:
        print([i,nums.index(remain)])