import csv
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from numpy import linspace
from matplotlib.pyplot import plot, xlabel, ylabel, show, rcParams

rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False

# df = np.loadtext(r"C:\Users\Administrator\Desktop\基金产品.csv", dtype=np.str, delimiter= ',')
df = pd.read_csv(r"d:\管理人.csv")
x = df.replace(0, np.nan)
t = x.dropna()
a = t.head(5)

df1 = a.rename(index=a['CnName'])

df1.plot(kind='bar')
show()
