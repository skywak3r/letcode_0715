# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

tmp1 = pd.date_range("2020-07-31 21:00",freq="500ms",end="2020-07-31 21:30")
tmp2= pd.date_range("2020-08-01 09:00",end="2020-08-01 9:30",freq="500ms")
ts = pd.Series(np.random.randn(tmp1.shape[0] ), index=tmp1)
ts2 = pd.Series(np.random.randn(tmp2.shape[0] ), index=tmp2)
df1 = pd.concat([ts,ts2],axis=1)

tmp1 = pd.date_range("2020-07-31 21:00",freq="s",end="2020-07-31 21:30")
tmp2= pd.date_range("2020-08-01 09:00",end="2020-08-01 9:30",freq="s")
ts = pd.Series(np.random.randn(tmp1.shape[0] ), index=tmp1)
ts2 = pd.Series(np.random.randn(tmp2.shape[0] ), index=tmp2)
df2 = pd.concat([ts,ts2],axis=1)

tmp1 = pd.date_range("2020-07-31 21:00",freq="5s",end="2020-07-31 21:30")
tmp2= pd.date_range("2020-08-01 09:00",end="2020-08-01 9:30",freq="5s")
ts = pd.Series(np.random.randn(tmp1.shape[0] ), index=tmp1)
ts2 = pd.Series(np.random.randn(tmp2.shape[0] ), index=tmp2)
df3 = pd.concat([ts,ts2],axis=1)

tmp1 = pd.date_range("2020-07-31 21:00",freq="10s",end="2020-07-31 21:30")
tmp2= pd.date_range("2020-08-01 09:00",end="2020-08-01 9:30",freq="10s")
ts = pd.Series(np.random.randn(tmp1.shape[0] ), index=tmp1)
ts2 = pd.Series(np.random.randn(tmp2.shape[0] ), index=tmp2)
df4 = pd.concat([ts,ts2],axis=1)



print(df1)
print(df2)
print(df3)
print(df4)

# tmp1= pd.date_range("2020-08-01 09:00",end="2020-08-01 9:30",freq="s")
# aa = pd.concat([df1,tmp1],axis=1)
# df1.append(tmp1)
# print(pd.concat([df1,tmp1],axis=1))