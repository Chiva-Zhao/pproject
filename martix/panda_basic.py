import numpy as np
from pandas import Series, DataFrame, concat


def serial_basic():
    a = np.random.randn(5)
    print("a is an array:")
    print(a)
    s = Series(a)
    print("s is a Series:")
    print(s)

    s = Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'], name='my_series')
    print(s)
    print(s.name)

    d = {'a': 0., 'b': 1, 'c': 2}
    print(d)
    s = Series(d)
    print("s is a Series:")
    print(s)

    s1 = Series(d, index=['b', 'c', 'd', 'a'])
    print(s1)
    s2 = Series(4., index=['a', 'b', 'c', 'd', 'e']);
    print(s2)

    s = Series(np.random.randn(10), index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
    print(s)
    print(s[0], s[:2])
    print(s[[2, 0, 4]])
    print(s[['e', 'i']])
    print(s[s > 0.5])
    print('e' in s)


def dataframe_basic():
    d = {'one': Series([1., 2., 3.], index=['a', 'b', 'c']),
         'two': Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
    df = DataFrame(d)
    print(df)
    df = DataFrame(d, index=['r', 'd', 'a'], columns=['two', 'three'])
    print(df)
    print(df.index)
    print(df.columns)
    print(df.values)

    d = {'one': [1., 2., 3., 4.], 'two': [4., 3., 2., 1.]}
    df = DataFrame(d, index=['a', 'b', 'c', 'd'])
    print(df)

    d = [{'a': 1.6, 'b': 2}, {'a': 3, 'b': 6, 'c': 9}]
    df = DataFrame(d)
    print(df)

    a = Series(range(5))
    b = Series(np.linspace(4, 20, 5))
    df = concat([a, b], axis=1)
    print(df)

    df = DataFrame()
    index = ['alpha', 'beta', 'gamma', 'delta', 'eta']
    for i in range(5):
        a = DataFrame([np.linspace(i, 5 * i, 5)], index=[index[i]])
        df = concat([df, a], axis=0)
    print(df)
    print(df.iloc[1])
    print(df.loc['beta'])




dataframe_basic();
