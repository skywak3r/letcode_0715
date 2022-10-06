# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

a = np.random.uniform(0,1000,(1000))
b = np.arange(0,1001)

A = pd.DataFrame(a)
B = pd.DataFrame(b)

# A.rolling(window=3,win_type="exponential")
A["Mean"] = A.rolling(window=3,win_type="exponential").mean()
B["Mean"] = B.rolling(window=3,win_type="exponential").mean()

A.reset_index(drop=True,).plot()
plt.show()

B.reset_index(drop=True,).plot()
plt.show()
print(A)
print(B)