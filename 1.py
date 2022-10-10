def judge(num):
    if num % 2:
        return True
    else:
        return False

import  numpy as np
nums = np.random.randint(0,100,100)
# print(nums)
print(list(filter(judge,nums)))