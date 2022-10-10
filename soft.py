import bisect
a = [1,2,3,4]
nums= [0,1,2,3,4,5]

for num in nums:
    index= bisect.bisect_left(a,num)
    print(num, index)