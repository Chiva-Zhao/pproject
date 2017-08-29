import pandas as pd

reader = pd.read_csv('gupiap.csv')
# reader['read'] = reader['read'].apply(lambda x: float(x))
sum = reader['read'].groupby(reader['name']).sum()
print(sum)
