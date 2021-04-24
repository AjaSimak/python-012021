import wget
#wget.download('https://raw.githubusercontent.com/pesikj/progr2-python/master/python-pro-data-1/agregace-a-spojovani/excs/assets/jmena.csv')
#wget.download('https://raw.githubusercontent.com/pesikj/progr2-python/master/python-pro-data-1/agregace-a-spojovani/excs/assets/studenti1.csv')
#wget.download('https://raw.githubusercontent.com/pesikj/progr2-python/master/python-pro-data-1/agregace-a-spojovani/excs/assets/studenti2.csv')

import pandas
jmena = pandas.read_csv("jmena.csv")
studenti_1 = pandas.read_csv("studenti.csv")
studenti_2 = pandas.read_csv("studenti2.csv")

#maturita = pandas.concat([u202, u203, u302],ignore_index=True)

# priklad 1
studenti = pandas.concat([studenti_1, studenti_2], ignore_index=True)
# index, aby se mi ignoroval index
#print(studenti.head())
#print(studenti_1.shape)
#print(studenti_2.shape)
#print(studenti.shape)

# priklad 2
#print(sum(studenti["ročník"].isnull()))
#print(sum(studenti["kruh"].isnull()))
#nevychází dle videa


# priklad 3
#studenti = studenti.dropna(subset=["ročník, "kruh"])

# priklad 4
print(studenti.groupby("obor").count())
print(studenti.groupby("obor").size())

# priklad 5
print(studenti.groupby("obor")["prospěch"].mean())

# priklad 6
print(pandas.merge(studenti, jmena, on=["jméno"]))
print(pandas.merge(studenti, jmena[["jméno", "pohlaví"]], on=["jméno"]))

# priklad 7
print(studenti.groupby("pohlaví").count())
print(studenti.groupby("pohlaví").size())
