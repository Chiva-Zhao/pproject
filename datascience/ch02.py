import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def select_filter(edu):
    edu.describe()
    edu[0:6]
    edu.ix[1:3, ['TIME', 'Value']]
    edu[edu['Value'] > 8.5]
    edu[edu['Value'].isnull()].head()
    edu[edu['TIME'] == 2011]
    edu.max(axis=0)
    print(" Pandas max function :", edu['Value'].max())
    print(" Python max function :", max(edu['Value']))


def manipulation(edu):
    s = edu["Value"] / 100
    s.head()
    s = edu["Value"].apply(np.sqrt)
    s.head()
    s = edu['Value'].apply(lambda x: x ** 2)
    s.head()
    edu['ValueNorm'] = edu['Value'] / edu['Value'].max()
    edu.tail()
    edu.drop('ValueNorm', axis=1, inplace=True)
    edu.tail()
    edu = edu.append({'TIME': 2015, 'Value': 10, 'GEO': 'Chiva'}, ignore_index=True, )
    edu.tail()
    edu.drop(max(edu.index), axis=0, inplace=True)
    edu.tail()
    droped = edu.drop(edu['Value'].isnull(), axis=0)
    droped.head()
    droped = edu.dropna(how='any', axis=0, subset=['Value'])
    droped.head()
    eduFilled = edu.fillna(axis=0, value={'Value': 0})
    eduFilled.head()


def sort_group(edu):
    edu.sort_values(by='Value', ascending=False, inplace=True)
    edu.head()
    edu.sort_index(inplace=True)
    edu.head()
    group = edu[['GEO', 'Value']].groupby(by=['GEO']).mean()
    group.head()


def pivot(edu):
    filtered = edu[edu['TIME'] > 2005]
    pivedu = pd.pivot_table(filtered, values='Value', index='GEO', columns='TIME')
    print(pivedu.head())


def rank(edu):
    pivedu = edu.drop([
        'Euro area (13 countries)',
        'Euro area (15 countries)',
        'Euro area (17 countries)',
        'Euro area (18 countries)',
        'European Union (25 countries)',
        'European Union (27 countries)',
        'European Union (28 countries)'
    ], axis=0)
    pivedu = pivedu.rename(index={'Germany (until 1990 former territory of the FRG)': 'Germany'})
    pivedu = pivedu.dropna()
    pivedu.rank(ascending=False, method='first').head()

    totalSum = pivedu.sum(axis=1)
    totalSum.rank(ascending=False, method='dense').sort_values().head()


def plotting(pivedu):
    totalSum = pivedu.sum(axis=1)
    totalSum.plot(kind='bar', style='b', alpha=0.4, title="Total Values for Country")
    my_colors = ['b', 'r', 'g', 'y', 'm', 'c']
    ax = pivedu.plot(kind='barh ',
                     stacked=True,
                     color=my_colors)
    ax.legend(loc='center left', bbox_to_anchor=(1, .5))


if (__name__ == '__main__'):
    edu = pd.read_csv('educ_figdp_1_Data.csv', na_values=':', usecols=['TIME', 'GEO', 'Value'])
    rank(edu)
