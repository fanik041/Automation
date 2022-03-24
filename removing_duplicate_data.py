mport numpy as np
import time
import openpyxl
import os
import collections
import csv
import pandas as pd
# C:\Users\Fahim Anik\PycharmProjects\SeleniumAutomation\venv\Lib\Selenium_Maps_Scraping
# path = 'C:/Users/Fahim Anik/PycharmProjects/SeleniumAutomation/venv/Lib/Selenium_Maps_Scraping/'

path = 'C:/Users/Fahim Anik/Users/Fahim Anik/Users/Fahim Anik/OneDrive - Advanced Symbolics/Desktop/cca-webscraping/SeleniumAutomation/venv/Lib/Selenium_Maps_Scraping/scraped_company_names/'


path2 = 'C:/Users/Fahim Anik/PycharmProjects/SeleniumAutomation/'
lists = []
lists_new = []
string = 'copy'
for filename in sorted(os.listdir(path)):
    if filename.startswith('Atlanta'):
        print("filename is ", filename)
        csv_name = path + filename
        df = pd.read_csv(csv_name)
        b = df.columns.values.tolist()
        print(b)
        df["0"] = df["0"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
        print(df["0"])
        x = df["0"].unique()
        for values in x:
            lists.append(values)
df1 = pd.DataFrame(lists, columns= ['names'])
df1 = df1['names'].unique()

for files in sorted(os.listdir(path2)):
    if files.endswith('abc.csv'):
        print("filename being compared to is ", files)
        csv_name1 = path2 + files
        df = pd.read_csv(csv_name1)
        b1 = df.columns.values.tolist()
        print(b1)
        df["Company Name"] = df["Company Name"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
        print(df["Company Name"])
        x = df["Company Name"].unique()
        for values in x:
            lists_new.append(values)
df = pd.DataFrame(lists_new, columns=['names'])
z = df['names'].unique()
csv1 = pd.DataFrame(z).to_csv("file-1.csv")
csv2 = pd.DataFrame(df1).to_csv("file-2.csv")
print("scraped company names are: ", z)
print("All company names are: ", df1)
print(len(z))
print(len(df1))
l1 = set(z)
l2 = set(df1)
vy = l2.difference(l1)
kl = pd.DataFrame(vy)
wy = np.array_split(kl, 5)
print(vy)
print(wy)
print(len(vy))
csv31 = pd.DataFrame(wy[0]).to_csv("file-31.csv")
csv32 = pd.DataFrame(wy[1]).to_csv("file-32.csv")
csv33 = pd.DataFrame(wy[2]).to_csv("file-33.csv")
csv34 = pd.DataFrame(wy[3]).to_csv("file-34.csv")
csv35 = pd.DataFrame(wy[4]).to_csv("file-35.csv")



