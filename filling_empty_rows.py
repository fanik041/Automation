import openpyxl
import os
import csv
import numpy as np
import pandas as pd

path = os.getcwd()
print(path)
from numpy import NaN
from itertools import tee, islice, chain


def previous_and_next(some_iterable):
    prevs, items, nexts = tee(some_iterable, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return zip(prevs, items, nexts)


# path = 'C:/Users/Fahim Anik/Users/Fahim Anik/Users/Fahim Anik/OneDrive - Advanced Symbolics/Desktop/cca-webscraping/SeleniumAutomation/venv/Lib/Selenium_Maps_Scraping/New folder/Vancouver/'

for filename in sorted(os.listdir(path)):
    # print("filename is ", filename)
    if filename.endswith('.csv'):
        csv_name = path + filename
        df = pd.read_csv(csv_name)
        df1 = df.iloc[:, 1:6]
        for columns in df[['Actual Company Name', 'Company Name', 'Company Rating', 'Company Details', 'Company Description', 'Total Reviews']]:
            x = []
            print(columns)
            for previous, rows, nxt in previous_and_next(df[columns]):
                x.append(rows)
                # print(x)
                if rows == 'None':
                    print("column is : ", columns)
                    # print("last element is :", last_elem)
                    # print("first element is: ", x[0])
                    print(filename)
                    df[columns] = df[columns].replace(rows, previous)
                    # print(rows)
                # elif rows == NaN:
                elif df[columns].isnull().values.any():
                    print("column with empty is : ", columns)
                    df[columns] = df[columns].replace(rows, previous)
                # if col == 'Company Rating':
                #     df['Company Rating'] = x[-1]
                # if col == 'Total Reviews':
                #     df['Total Reviews'] = x[-1]
                # df[col] = df[col].replace(r, y[-1])
                # elif columns=='':
        # df2 = df[['Company Description', 'Reviewer Name', 'Reviewer Comment', 'Reviewer Rating']]
        # df1['Company Rating']=df1['Company Rating'].astype(object)
        # df1['Company Description']=df1['Company Description'].astype(object)
        # dataTypeDict = dict(df2.dtypes)
        # dataTypeDict1 = dict(df1.dtypes)
        # print("first df: ", dataTypeDict)
        # print("second df: ", dataTypeDict1)
        # for columns in df1:
        #     print("first df: ", columns, type(df1[columns]))
        # for column in df2:
        #     print("Seccond df: ", column, type(df2[column]))
        # df3 = df1.merge(df2, on='Company Description')
        # print(df3)
        df.to_csv(path + "/scraped_reviews/" + filename)
        # print(df)
