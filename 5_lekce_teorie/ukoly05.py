#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/nacteni-dat/excs/nabidky/assets/DataAnalyst.csv")

import pandas
jobs = pandas.read_csv('DataAnalyst.csv')

#první úkol
print(jobs.head())

#druhý úkol
print(jobs.columns)

#třetí úkol
print(jobs.shape[0])

#čtvrtý úkol
print(jobs.iloc[9])

#pátý úkol
print(jobs.iloc[11:20, 6])

