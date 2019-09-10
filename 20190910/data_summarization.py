import datetime
import random

import numpy as np
import pandas as pd
from sklearn import preprocessing


def generate_sample_data(row_count=100):
    """
    This function generates a random transaction dataset

    :param row_count: number of rows generated datas
    :return: a pandas dataframe
    """
    startDate = datetime.datetime(2019, 9, 6, 19)
    serial_number_sentinel = 1000
    user_id_sentinel = 5001
    product_id_sentinel = 101
    price_sentinel = 2000
    # base list of attributes
    data_dict = {
        'Serial No': np.arange(row_count) + serial_number_sentinel,
        'Date': np.random.permutation(pd.to_datetime([x.strftime("%d-%m-%Y")
                                                      for x in _random_date(startDate,
                                                                            row_count)]).date
                                      ),
        'User ID': np.random.permutation(np.random.randint(0,
                                                           row_count,
                                                           size=int(row_count / 10)) + user_id_sentinel).tolist() * 10,
        'Product ID': np.random.permutation(np.random.randint(0,
                                                              row_count,
                                                              size=int(
                                                                  row_count / 10)) + product_id_sentinel).tolist() * 10,
        'Quantity Purchased': np.random.permutation(np.random.randint(1,
                                                                      42,
                                                                      size=row_count)),
        'Price': np.round(np.abs(np.random.randn(row_count) + 1) * price_sentinel,
                          decimals=2),
        'User Type': np.random.permutation([chr(random.randrange(97, 97 + 3 + 1))
                                            for i in range(row_count)])
    }
    # introduce missing values
    for index in range(int(np.sqrt(row_count))):
        data_dict['Price'][np.argmax(data_dict['Price'] == random.choice(data_dict['Price']))] = np.nan
        data_dict['User Type'][np.argmax(data_dict['User Type'] == random.choice(data_dict['User Type']))] = np.nan
        data_dict['Date'][np.argmax(data_dict['Date'] == random.choice(data_dict['Date']))] = np.nan
        data_dict['Product ID'][np.argmax(data_dict['Product ID'] == random.choice(data_dict['Product ID']))] = 0
        data_dict['Serial No'][np.argmax(data_dict['Serial No'] == random.choice(data_dict['Serial No']))] = -1
        data_dict['User ID'][np.argmax(data_dict['User ID'] == random.choice(data_dict['User ID']))] = -101

    # create data frame
    df = pd.DataFrame(data_dict)

    return df


def _random_date(start, date_count):
    """This function generates a random date based on params
    Args:
        start (date object): the base date
        date_count (int): number of dates to be generated
    Returns:
        list of random dates

    """
    current = start
    while date_count > 0:
        curr = current + datetime.timedelta(days=random.randrange(42))
        yield curr
        date_count -= 1


df = generate_sample_data(row_count=1000)
# Dataset with columns renamed
def cleanup_column_names(df: pd.DataFrame, rename_dict={}, inplaced=True):
    """
    This function renames columns of a pandas dataframe
    It converts column names to snake case if rename_dict is not passed

    :param df:
    :param rename_dict: keys represent old column names and values point to newer ones
    :param inplaced: flag to update existing dataframe or return a new one
    :return: pandas dataframe if inplace is set to False, None otherwise
    """
    if not rename_dict:
        return df.rename(columns={col: col.lower().replace(' ', '_') for col in df.columns.values.tolist()},
                         inplace=inplaced)
    else:
        return df.rename(columns=rename_dict, inplace=inplaced)


cleanup_column_names(df)

# Transformations
def expand_user_type(type):
    if type in ['a', 'b']:
        return 'new'
    elif type == 'c':
        return 'existing'
    elif type == 'd':
        return 'loyal_existing'
    else:
        return 'error'

df['date'] = pd.to_datetime(df.date)
df['user_class'] = df['user_type'].map(expand_user_type)
df['purchase_week'] = df[['date']].applymap(lambda dt: dt.week if not pd.isnull(dt) else 0)

# Normalizing Numeric Values
# Normalize price values using Min-Max Scaler
df_normalized = df.dropna().copy()
min_max_scaler = preprocessing.MinMaxScaler()
np_scaled = min_max_scaler.fit_transform(df_normalized['price'].values.reshape(-1, 1))
df_normalized['normalized_price'] = np_scaled.reshape(-1, 1)
# Normalize quantity purchased values using Robust Scaler
df_normalized = df.dropna().copy()
robust_scaler = preprocessing.RobustScaler()
rs_scaled = robust_scaler.fit_transform(df_normalized['quantity_purchased'].values.reshape(-1, 1))
df_normalized['quantity_purchased'] = rs_scaled.reshape(-1, 1)
# Condition based aggregation
print("Mean price of items purchased by user_type=a :: {}".format(df['price'][df['user_type'] == 'a'].mean()))
# Condtion based counts
print(df['purchase_week'].value_counts())
# Group By certain attributes
print(df.groupby(['user_class'])['quantity_purchased'].sum())
# Group By with different aggregate functions
print(df.groupby(['user_class'])['quantity_purchased'].agg([np.sum, np.mean, np.count_nonzero]))
# Group by specific aggregate functions for each attribute
df.groupby(['user_class', 'user_type']).agg({'price': np.mean, 'quantity_purchased': np.max})
# Group by with multiple agg for each attribute
df.groupby(['user_class', 'user_type']).agg({'price': {
    'total_price': np.sum,
    'mean_price': np.mean,
    'variance_price': np.std,
    'count': np.count_nonzero},
    'quantity_purchased': np.sum})
# pivot tables
df.pivot_table(index='date', columns='user_type', values='price', aggfunc=np.mean)
# Stack a Dataframe
df.stack()
