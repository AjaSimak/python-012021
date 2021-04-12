#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/vykazy.csv")

import pandas
vykazy = pandas.read_csv("vykazy.csv")
hodiny = vykazy.groupby("project")["hours"].sum()
#hodiny.to_excel("hodiny.xlsx", index=False)
zamestnanci = pandas.read_csv("zamestnanci.csv")


#print(vykazy.loc[1])
#print(hodiny)

#print(vykazy.head())
#print(zamestnanci.head())

vykazy_zamestnanci = pandas.merge(vykazy, zamestnanci, how="cross")
#print(vykazy_zamestnanci.columns)
#print(vykazy_zamestnanci)
hodiny_projekt = vykazy_zamestnanci.groupby(["mesto", "project"])["hours"].sum()
print(hodiny_projekt)

