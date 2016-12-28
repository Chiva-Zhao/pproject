import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
from numpy import linspace
from matplotlib.pyplot import plot, xlabel, ylabel, show, rcParams

rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False
#plt.figure(figsize=(60, 20))
#fig = plt.figure(figsize=(3, 3))
#ax = fig.add_subplot(1, 1, 1, frameon=True)

df = pd.read_csv(r"基金专户产品.csv")
a = df.set_index('RegisterDate')
h = df.groupby(['ManagerCnName','RegisterDate']).sum()
# h.plot(figsize=(20, 10))
df2 = df.groupby(['ManagerCnName']).sum()
s = df2.head(10).plot(figsize=(20, 10))
#h.plot()
# plt.savefig('test.png')
plt.savefig('test.pdf')
plt.show()
plt.close()