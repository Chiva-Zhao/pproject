import json
import pandas as pd

jsonFileData = open('sample_json.json').read()
jsonData = json.loads(jsonFileData)
print(jsonData['outer_col_3'])
df = pd.read_json('pandas_json.json', orient='records')
print(df)