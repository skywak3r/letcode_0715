import pandas as pd
import numpy as np
from matplotlib import pyplot as plt



a = np.random.uniform(0,1000,(1000))
b = np.arange(0,1001)

A = pd.DataFrame(a)
B = pd.DataFrame(b)

# A.rolling(window=3,win_type="exponential")
A["Mean"] = A.rolling(window=3,win_type="exponential").mean()
B["Mean"] = B.rolling(window=3,win_type="exponential").mean()

nums = A.iloc[:,0]
# nums = np.array([2,3,1,2,3,2,1])


# df = pd.DataFrame(nums)
pre = [nums[0]]
for i in range(1,len(nums)):
    pre.append(nums[i] - nums[i-1])
flipHistory = [nums[0]]

for i in range(1,len(pre)):
    index = i - 1
    cur = 0
    cur = pre[i]
    while  index>0 and pre[i] * pre[index] >0:
        cur += pre[index]
        index -= 1
    flipHistory.append(cur)
# print(flipHistory)


# print(flipHistory)
A["flip_history"] = pd.DataFrame(flipHistory)

tmp = A["flip_history"]
print(tmp.groupby(20))