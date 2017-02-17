import numpy as np
import pandas as pd
from pandas import Series, DataFrame


def basic1():
    dates = pd.date_range('20150101', periods=5)
    print(dates)
    df = pd.DataFrame(np.random.randn(5, 4), index=dates, columns=list('ABCD'))
    print(df)
    df2 = pd.DataFrame(
        {'A': 1., 'B': pd.Timestamp('20150214'), 'C': pd.Series(1.6, index=list(range(4)), dtype='float64'),
         'D': np.array([4] * 4, dtype='int64'), 'E': 'hello pandas!'})
    print(df2)


basic1()
