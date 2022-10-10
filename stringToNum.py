import pandas as pd
import numpy as np

time_idx=  pd.period_range("2022-01-01",end="2022-02-01",freq="D")
values = np.random.random(len(time_idx))
print(time_idx)
print(values)
df = pd.DataFrame(values,index=time_idx)
df["mean_3"] = df[0].rolling(window=3,center=True).mean()
print(df)
print(df.dropna())
# df["mean_3"] =
