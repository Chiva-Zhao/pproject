import datetime

import pandas as pd
import numpy as np

# List of Dictionaries to Dataframe
d = [{'city': 'Delhi', "data": 1000},
     {'city': 'Bangalore', "data": 2000},
     {'city': 'Mumbai', "data": 1000}]
# print(pd.DataFrame(d))
# CSV Files to Dataframe
city_data = pd.read_csv('worldcities.csv')
# print(city_data.head(10))
# Databases to Dataframe
import mysql.connector

# mysqlCon = mysql.connector.connect(
#     user="root",
#     password="XXXXXX",
#     host="127.0.0.1",
#     port=3306,
#     database="mysql"
# )
# data = pd.read_sql("select * from user", mysqlCon)
# print(data)
# mysqlCon.close()
from sqlalchemy import create_engine

# conn = create_engine(
#     "mysql+mysqlconnector://root:cz186008@localhost/auto_code"
# )
# users = pd.DataFrame({
#     "username": ["test1", "test2"],
#     "password": ["test3", "test4"],
#     "add_time": [datetime.datetime.now(), datetime.datetime.now()]
# })
# users.to_sql("back_user", conn, if_exists='append',index=False)

# print(city_data.tail(3))
# series_es = city_data.lat
# print(type(series_es))
# print(series_es[1:10:2])
# print(series_es[:7])
# print(series_es[:-7790])
# print(city_data[:5])
# print(city_data.iloc[:5,:4])
# print(city_data.columns)
# sub_data = city_data[city_data['population'] > 10000000][city_data.columns[pd.Series(city_data.columns).str.startswith('l')]]
# print(sub_data)
# city_greater_10mil = city_data[city_data['population'] > 10000000]
# print(city_greater_10mil.where(city_greater_10mil.population > 15000000))

# Values Attribute
df = pd.DataFrame(np.random.rand(8, 3), columns=["A", "B", "C"])
nparray = df.values
# print(type(nparray))
df.iloc[4, 2] = None
# print(df)
# print(df.fillna(0))

# Descriptive Statistics Functions
columns_numeric = ['lat', 'lng', 'population']
# print(city_data[columns_numeric].mean())
# print(city_data[columns_numeric].sum())
# print(city_data[columns_numeric].count())
# print(city_data[columns_numeric].median())
# print(city_data[columns_numeric].quantile(0.8))
# print(city_data[columns_numeric].sum(axis=1))
# print(city_data[columns_numeric].describe())

# Concatenating Using the concat Method
# city_data1 = city_data.sample(3)
# city_data2 = city_data.sample(3)
# city_data_combine = pd.concat([city_data1,city_data2])
# print(city_data_combine)

df1 = pd.DataFrame({'col1': ['col10', 'col11', 'col12', 'col13'],
                    'col2': ['col20', 'col21', 'col22', 'col23'],
                    'col3': ['col30', 'col31', 'col32', 'col33'],
                    'col4': ['col40', 'col41', 'col42', 'col43']},
                   index=[0, 1, 2, 3])
df4 = pd.DataFrame({'col2': ['col22', 'col23', 'col26', 'col27'],
                    'Col4': ['Col42', 'Col43', 'Col46', 'Col47'],
                    'col6': ['col62', 'col63', 'col66', 'col67']},
                   index=[2, 3, 6, 7])
# print(pd.concat([df1, df4], axis=1))

# Database Style Concatenations Using the merge Command
country_data = city_data[['iso3','country']].drop_duplicates()
del(city_data['country'])
print(city_data.merge(country_data,how='inner').head())