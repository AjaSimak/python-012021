#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/vykazy.csv")

import pandas
vykazy = pandas.read_csv("vykazy.csv")
hodiny = vykazy.groupby("project")["hours"].sum()
#hodiny.to_excel("hodiny.xlsx", index=False)
zamestnanci = pandas.read_csv("zamestnanci.csv")


print(vykazy.loc[1])
print(hodiny)

print(vykazy.head())
print(zamestnanci.head())

vykazy_zamestnanci = pandas.merge(vykazy, zamestnanci, how="cross")
print(vykazy_zamestnanci.columns)
print(vykazy_zamestnanci)

#vykazy_zamestnanci_1= pandas.merge(vykazy, zamestnanci, how="left", on="emloyee_id"=="cislo_zamestnance")
#print(vykazy_zamestnanci_1)

#Následně proveď statistiku vykázaných hodin za jednotlivé kanceláře,
# tj. spočítej celkový počet hodin vykázaný zaměstnanci jednotlivých kanceláří na projekty daného zákazníka.
# dotaz: co je jednotlivá kancelář? město?
# dotaz2: je totožný sloupec "employee_id" a "cislo_zamestnance"? ráda bych to použila pro merge, jen nevím...,
# ...jak to udělat,když se jmenují odlišně -> jak je přejmenovat? nebo se to píše nějak do on="employee_id"="cislo_zamestnance"?

