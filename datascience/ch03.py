# Descriptive Statistics
import pandas as pd


def read_data():
    file = open('adult.data', 'r')

    def chr_int(a):
        if a.isdigit():
            return int(a)
        else:
            return 0

    data = []
    for line in file:
        data1 = line.split(', ')
        if len(data1) == 15:
            data.append([chr_int(data1[0]), data1[1],
                         chr_int(data1[2]), data1[3],
                         chr_int(data1[4]), data1[5],
                         data1[6], data1[7], data1[8],
                         data1[9], chr_int(data1[10]),
                         chr_int(data1[11]),
                         chr_int(data1[12]),
                         data1[13], data1[14]
                         ])
    print(data[1:2])
    df = pd.DataFrame(data)
    df.columns = [
        'age', 'type_employer', 'fnlwgt',
        'education', 'education_num', 'marital',
        'occupation', 'relationship', 'race',
        'sex', 'capital_gain', 'capital_loss',
        'hr_per_week', 'country', 'income'
    ]
    print(df.shape)
    counts = df.groupby('country').size()
    # print(counts.head)
    ml = df[df['sex'] == 'Male']
    # print(male.head())
    ml1 = df[(df['sex'] == 'Male') & (df['income'] == '>50K\n')]
    # print(male_high_income.head())
    fm = df[df['sex'] == 'Female']
    fm1 = df[(df['sex'] == 'Female') & (df['income'] == '>50K\n')]
    df1 = df[(df.income == '>50K\n')]
    print('The rate of people with high income is : ', int(len(df1) / float(len(df)) * 100), '%. ')
    print('The rate of men with high income is : ', int(len(ml1) / float(len(ml)) * 100), '%. ')
    print('The rate of women with high income is : ', int(len(fm1) / float(len(fm)) * 100), '%. ')


read_data()
