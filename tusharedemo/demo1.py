import tushare as ts
import pandas as pd
import numpy as np

a = ts.get_today_all()
c = a.sort(['changepercent'], ascending=False)
df5 = c[(c.changepercent > 0) & (c.changepercent < 5)]
print(len(df5))
df6 = df5.reindex(range(0, len(df5)))
# df6 = df5.reindex(pd.Index(range(0,len(df5))))
print(df6)
