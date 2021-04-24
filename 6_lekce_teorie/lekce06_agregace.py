import pandas

#import wget
#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/nacteni-dat/assets/nakupy.csv")

u202 = pandas.read_csv("u202.csv").dropna()
u203 = pandas.read_csv("u203.csv").dropna()
u302 = pandas.read_csv("u302.csv").dropna()
u202["mistnost"] = "u202"
u203["mistnost"] = "u203"
u302["mistnost"] = "u302"
maturita = pandas.concat([u202, u203, u302], ignore_index=True)

#print(maturita.groupby("mistnost").count())

#print(maturita.groupby("predmet").mean())
#mean je průměr
#udělalo to průměr ze všech čísel (i z čísla studenta)

#print(maturita.groupby("predmet")["znamka"].mean())

#print(maturita.groupby("predmet")["znamka"].max())
#ukáže mi, kdo vylítl z maturity z jakého předmětu

#print(maturita.groupby("predmet")["znamka"].sum())


#příklad na nákupy, ještě bych mohla napsat specifický sloupec s těmi cenami, ale je tam jen jeden, tak nemusím jej psát
nakupy = pandas.read_csv("nakupy.csv")
print(nakupy.groupby("Jméno").sum())

