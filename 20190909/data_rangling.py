import datetime
import random

import numpy as np
import pandas as pd


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
# basic information
print("Number of rows::", df.shape[0])
print("Number of columns::", df.shape[1])
print("Column Names::", df.columns.values.tolist())
print("Column Data Types::\n", df.dtypes)

# some missing value row/columns
print("Columns with Missing Values::", df.columns[df.isnull().any()].tolist())
print("Number of rows with Missing Values::", len(df.isnull().any(1).to_numpy().nonzero()[0].tolist()))
print("Sample Indices with missing data::", df.isnull().any(1).to_numpy().nonzero()[0].tolist()[0:5])

print("General Stats::")
print(df.info())
print("Summary Stats::")
print(df.describe())


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
print("Dataframe columns:\n{}".format(df.columns.tolist()))

# Filtering Columns
# print 10 values from column at index 3
print(df.iloc[:, 3].values[0:10])
print("Using Column Name::")
print(df.quantity_purchased.values)
print("Using Column Data Type::")
print(df.select_dtypes(include=['float64']).values[:, 0])
# Filtering Rows
print("Select Specific row indices::")
print(df.iloc[[10, 501, 20]])
print("Excluding Specific Row indices::")
print(df.drop([0, 24, 51], axis=0).head())
print("Subsetting based on logical condition(s)::")
print(df[df.quantity_purchased > 25].head())
print("Subsetting based on offset from top (bottom)::")
print(df[100:].head())  # df.tail(-100)

# Typecasting
df['date'] = pd.to_datetime(df.date)
print(df.date)


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


df['user_class'] = df['user_type'].map(expand_user_type)
df['purchase_week'] = df[['date']].applymap(lambda dt: dt.week if not pd.isnull(dt) else 0)
df.select_dtypes(include=['number']).apply(lambda x: x.max() - x.min())

# Imputing Missing Values
print("Drop Rows with missing dates::")
# Drop Rows with missing dates
df_dropped = df.dropna(subset=['date'])
print("Fill Missing Price values with mean price::")
df_dropped['price'].fillna(np.round(df['price'].mean(), 2), inplace=True)
print("Fill Missing user_type values with value from previous row (forward fill) ::")
df_dropped['user_type'].fillna(method='ffill', inplace=True)
print("Fill Missing user_type values with value from next row (backward fill) ::")
df_dropped['user_type'].fillna(method='bfill', inplace=True)

# Handling Duplicates
# sample duplicates
df_dropped[df_dropped.duplicated(subset=['serial_no'])]
df_dropped.drop_duplicates(subset=['serial_no'], inplace=True)

# Handling Categorical Data
# using map to dummy encode
type_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3, np.NAN: -1}
df['encoded_user_type'] = df.user_type.map(type_map)
# using get_dummies to one hot encode
print(pd.get_dummies(df,columns=['user_type']).head())
# Normalizing Values